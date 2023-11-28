from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Markup, Statistic


markup_crud = CRUDBase(Markup)
statistic_crud = CRUDBase(Statistic)
