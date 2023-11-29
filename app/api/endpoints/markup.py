from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.markup import markup_crud
from app.core.db import get_async_session
from app.schemas.markup import MarkupCreate, MarkupDB
from app.core.user import current_user


router = APIRouter()


@router.get(
    '/',
    response_model=List[MarkupDB],
    dependencies=[Depends(current_user)],
)
async def get_recomendations(
    session: AsyncSession = Depends(get_async_session),
):
    recomendations = await markup_crud.get_multi(session)
    return recomendations


@router.post(
    '/',
    response_model=List[MarkupDB],
    dependencies=[Depends(current_user)],
)
async def create_recomendations(
    data: List[MarkupCreate],
    session: AsyncSession = Depends(get_async_session),
):
    await markup_crud.create_multi(data, session)
    return data


@router.get(
    '/{dealer_price_id}',
    response_model=List[MarkupDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
)
async def get_recomendations_by_dealer_price(
    dealer_price_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    dealer_price = await check_dealer_price_exists(dealer_price_id, session)
    markup = await markup_crud.get_markup_by_dealer_price(dealer_price, session)
    return markup
