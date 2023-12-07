from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.markup import statistic_crud
from app.core.db import get_async_session
from app.schemas.markup import StatisticCreate, StatisticInfo, StatisticDB
from app.core.user import current_user, current_superuser
from app.api.validators import check_exists


router = APIRouter()


@router.get(
    '/',
    response_model=List[StatisticInfo],
    dependencies=[Depends(current_user)],
)
async def get_statistic(
    session: AsyncSession = Depends(get_async_session),
):
    statistic = await statistic_crud.get_statistic(session)
    return statistic


@router.post(
    "/",
    response_model=StatisticDB,
    dependencies=[Depends(current_user)]
)
async def create_statistic(
    product_in: StatisticCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await statistic_crud.create(product_in, session)


@router.delete('/{statistic_id}', response_model=StatisticDB,
               dependencies=[Depends(current_superuser)])
async def delete_statistic_id(
        statistic_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    statistic = await check_exists(
        statistic_id, session, statistic_crud
    )
    statistic = await statistic_crud.remove(statistic, session)
    return statistic
