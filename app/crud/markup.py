from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Markup, Statistic, DealerPrice


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


markup_crud = CRUDMarkup(Markup)
statistic_crud = CRUDBase(Statistic)
