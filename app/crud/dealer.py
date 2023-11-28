from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Dealer, DealerPrice


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

    async def get_product_by_dealer(
        self,
        dealer: Dealer,
        session: AsyncSession
    ) -> Optional[List[DealerPrice]]:
        db_objs = await session.execute(select(self.model).where(
            self.model.dealer_id == dealer.id
        ))
        return db_objs.scalars().all()


dealer_crud = CRUDDealer(Dealer)
dealerprice_crud = CRUDBase(DealerPrice)
