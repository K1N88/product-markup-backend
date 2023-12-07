from datetime import date
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import (Dealer, DealerPrice, Statistic, ProductDealerKey,
                        Product)


class CRUDDealer(CRUDBase):

    async def create_multi(
        self,
        obj_in,
        session: AsyncSession,
    ) -> List[Dealer]:
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
        session: AsyncSession,
        name: Optional[str] = None,
        state: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> Optional[List]:
        stmt = select(self.model, Dealer.name, Statistic.state, Product).\
            where(self.model.dealer_id == dealer.id).\
            join(Dealer).\
            outerjoin(Statistic).\
            outerjoin(ProductDealerKey,
                      self.model.id == ProductDealerKey.key).\
            outerjoin(Product, ProductDealerKey.product_id == Product.id)

        if name:
            stmt = stmt.filter(self.model.product_name.ilike(f'%{name}%'))
        if state:
            stmt = stmt.filter(Statistic.state == state)
        if start_date:
            stmt = stmt.filter(self.model.date >= start_date)
        if end_date:
            stmt = stmt.filter(self.model.date <= end_date)

        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            price, dealer_name, status, product = item
            result.append(
                {
                    'dealerprice': price.__dict__,
                    'dealer': dealer_name,
                    'state': status,
                    'product': product
                }
            )
        return result

    async def get_multi_products(
        self,
        session: AsyncSession,
        name: Optional[str] = None,
        state: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> Optional[List]:
        stmt = select(self.model, Dealer.name, Statistic.state, Product).\
            join(Dealer).\
            outerjoin(Statistic).\
            outerjoin(ProductDealerKey,
                      self.model.id == ProductDealerKey.key).\
            outerjoin(Product, ProductDealerKey.product_id == Product.id)

        if name:
            stmt = stmt.filter(self.model.product_name.ilike(f'%{name}%'))
        if state:
            stmt = stmt.filter(Statistic.state == state)
        if start_date:
            stmt = stmt.filter(self.model.date >= start_date)
        if end_date:
            stmt = stmt.filter(self.model.date <= end_date)

        db_objs = await session.execute(stmt)
        result = []
        for item in db_objs:
            price, dealer_name, status, product = item
            result.append(
                {
                    'dealerprice': price.__dict__,
                    'dealer': dealer_name,
                    'state': status,
                    'product': product
                }
            )
        return result


dealer_crud = CRUDDealer(Dealer)
dealerprice_crud = CRUDDealerPrice(DealerPrice)
