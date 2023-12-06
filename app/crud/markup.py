from typing import Optional, List

from tqdm import tqdm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.crud.dealer import dealerprice_crud
from app.crud.product import product_crud
from app.models import Markup, Statistic, DealerPrice
from app.core.ml_prosept import prosept_predict
from app.core.setup_logger import setup_logger


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
    ) -> Optional[List[Markup]]:
        db_objs = await session.execute(
            select(self.model)
            .where(self.model.key == dealer_price.id)
            .order_by(self.model.queue)
        )
        return db_objs.scalars().all()

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
        logger.info(obj_in[:10])

        count = 0
        db_objs = []
        '''for item in tqdm(obj_in):
            # item["key"] = item.pop("id")
            db_obj = self.model(**item)
            db_objs.append(db_obj)
            session.add(db_obj)
            count += 1
        await session.commit()'''
        message = f'Создано {count} объектов {Markup}'
        logger.info(message)
        return message


class CRUDStatistic(CRUDBase):

    async def get_statistic(
        self,
        session: AsyncSession
    ) -> Optional[List]:
        stmt = select(self.model, Markup).join(Markup)
        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            statistic, markup = item
            result.append(
                {
                    'statistic': statistic.__dict__,
                    'markup': markup.__dict__,
                }
            )
        return result


markup_crud = CRUDMarkup(Markup)
statistic_crud = CRUDStatistic(Statistic)
