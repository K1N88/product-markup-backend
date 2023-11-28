from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Dealer


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


dealer_crud = CRUDDealer(Dealer)
