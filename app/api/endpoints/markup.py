from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.dealer import markup_crud, statistic_crud
from app.core.db import get_async_session
from app.schemas.markup import MarkupDB, StatisticDB
from app.core.user import current_user


logger = setup_logger()

router = APIRouter()


@router.get(
    '/markup',
    response_model=List[MarkupDB],
    dependencies=[Depends(current_user)],
)
async def get_all_recomendations(
    session: AsyncSession = Depends(get_async_session),
):
    recomendations = await markup_crud.get_multi(session)
    return recomendations


@router.get(
    '/statistic',
    response_model=List[StatisticDB],
    dependencies=[Depends(current_user)],
)
async def get_statistic(
    session: AsyncSession = Depends(get_async_session),
):
    statistic = await statistic_crud.get_multi(session)
    return statistic
  
