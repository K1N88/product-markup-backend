from sqlalchemy import and_, between, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Dealer


class CRUDDealer(CRUDBase):

    async def create_multi(
        self,
        obj_in,
        session: AsyncSession
    ):
        for item in obj_in:
            obj_in_data = item.dict()
            db_obj = self.model(**obj_in_data)
            session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


dealer_crud = CRUDDealer(Dealer)
