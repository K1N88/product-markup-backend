from itertools import count
from typing import Optional, List

from tqdm import tqdm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.crud.dealer import dealerprice_crud
from app.crud.product import product_crud
from app.models import Markup, Statistic, DealerPrice, Product, Statistic
from app.core.ml_prosept_vector import prosept_predict
from app.core.setup_logger import setup_logger
from app.models.markup import Choice


logger = setup_logger()


class CRUDMarkup(CRUDBase):

    async def create_multi(
        self,
        obj_in,
        session: AsyncSession,
    ) -> list[Markup]:
        db_objs = []
        for item in obj_in:
            obj_in_data = item.dict()
            db_obj = self.model(**obj_in_data)
            db_objs.append(db_obj)
            session.add(db_obj)
        await session.commit()
        return db_objs

    async def get_markup_by_dealer_price(
        self,
        dealer_price: DealerPrice,
        session: AsyncSession
    ) -> Optional[List]:
        stmt = select(self.model, Product).\
            where(self.model.key == dealer_price.id).\
            join(Product).\
            order_by(self.model.queue)
        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            markup, product = item
            result.append(
                {
                    'markup': markup.__dict__,
                    'product': product.__dict__,
                }
            )
        return result

    async def create_predict(
        self,
        session: AsyncSession,
    ) -> list[Markup]:
        product = await product_crud.get_multi(session),
        dealerprice = await dealerprice_crud.get_multi(session),

        product_df, dealerprice_df = [], []

        for item in product[0]:
            item = item.__dict__
            item.pop('_sa_instance_state')
            product_df.append(item)

        for item in dealerprice[0]:
            item = item.__dict__
            item.pop('_sa_instance_state')
            dealerprice_df.append(item)

        logger.info('start predict')
        obj_in = prosept_predict(
            product=product_df,
            dealerprice=dealerprice_df,
        )
        logger.info('finish predict')
        # logger.info(obj_in[:10])

        count = 0
        db_objs = []
        for item in tqdm(obj_in):
            item["key"] = item.pop("id")
            db_obj = self.model(**item)
            db_objs.append(db_obj)
            session.add(db_obj)
            count += 1
        await session.commit()
        message = f'Создано {count} объектов {Markup}'
        logger.info(message)
        return message


class CRUDStatistic(CRUDBase):

    async def get_statistic(
        self,
        session: AsyncSession
    ):
        stmt = select(self.model, Markup).join(Markup)
        db_objs = await session.execute(stmt)
        print(db_objs)
        result = {}
        yes = 0
        no = 0
        hold = 0
        for item in db_objs:
            statistic, markup = item
            f = select(Statistic).where(Statistic.markup == statistic.markup, Statistic.state == Choice.YES)
            db = await session.execute(f)
            for i in db:
                yes += 1
            f = select(Statistic).where(Statistic.markup == statistic.markup, Statistic.state == Choice.NO)
            db = await session.execute(f)
            for i in db:
                no += 1
            f = select(Statistic).where(Statistic.markup == statistic.markup, Statistic.state == Choice.HOLD)
            db = await session.execute(f)
            for i in db:
                hold += 1
        total = yes + no + hold
        result ={'yes': yes, 'no': no, 'hold': hold, 'total': total}
        
        return result


markup_crud = CRUDMarkup(Markup)
statistic_crud = CRUDStatistic(Statistic)
