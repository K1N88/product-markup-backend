from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.dealer import dealer_crud
from app.core.db import get_async_session
from app.schemas.dealer import DealerDB
from app.core.user import current_user


router = APIRouter()


@router.get(
    '/',
    response_model=List[DealerDB],
    dependencies=[Depends(current_user)],
)
async def get_all_dealers(
    session: AsyncSession = Depends(get_async_session),
):
    dealers = await dealer_crud.get_multi(session)
    return dealers


@router.post(
    '/',
    response_model=List[DealerDB],
    dependencies=[Depends(current_user)],
)
async def create_all_dealers(
    data: List[DealerDB],
    session: AsyncSession = Depends(get_async_session),
):
    await dealer_crud.create_multi(data, session)
    return data
