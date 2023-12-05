from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Dealer, DealerPrice, Statistic


class CRUDDealer(CRUDBase):

    async def create_multi(
        self,
        obj_in,
        session: AsyncSession,
    ) -> list[Dealer]:
        db_objs = []
        for item in obj_in:
            obj_in_data = item.dict()
            db_obj = self.model(**obj_in_data)
            db_objs.append(db_obj)
            session.add(db_obj)
        await session.commit()
        return db_objs


class CRUDDealerPrice(CRUDBase):

    async def get_all_products_by_dealer(
        self,
        dealer: Dealer,
        session: AsyncSession
    ) -> Optional[List]:
        stmt = select(self.model, Dealer.name, Statistic.state).\
            join(Dealer).\
            outerjoin(Statistic).\
            filter(self.model.dealer_id == dealer.id)
        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            price, name, state = item
            result.append(
                {
                    'dealerprice': price.__dict__,
                    'dealer': name,
                    'state': state
                }
            )
        return result

    async def get_multi_products(
        self,
        session: AsyncSession
    ) -> Optional[List]:
        stmt = select(self.model, Dealer.name, Statistic.state).\
            join(Dealer).\
            outerjoin(Statistic)
        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            price, name, state = item
            result.append(
                {
                    'dealerprice': price.__dict__,
                    'dealer': name,
                    'state': state
                }
            )
        return result


dealer_crud = CRUDDealer(Dealer)
dealerprice_crud = CRUDDealerPrice(DealerPrice)
