from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate

from app.crud.markup import markup_crud
from app.core.db import get_async_session
from app.schemas.markup import MarkupCreate, MarkupDB
from app.core.user import current_user
from app.api.validators import check_dealer_price_exists


router = APIRouter()


@router.get(
    '/',
    response_model=Page[MarkupDB],
    dependencies=[Depends(current_user)]
)
async def get_recomendations(
    session: AsyncSession = Depends(get_async_session)
):
    markup = await markup_crud.get_multi(session)
    return paginate(markup)


@router.post(
    '/',
    response_model=List[MarkupDB],
    dependencies=[Depends(current_user)]
)
async def create_recomendations(
    session: AsyncSession = Depends(get_async_session)
):
    predict = await markup_crud.create_predict(session)
    return predict


@router.get(
    '/{dealer_price_id}',
    response_model=Page[MarkupDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)]
)
async def get_recomendations_by_dealer_price(
    dealer_price_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    dealer_price = await check_dealer_price_exists(dealer_price_id, session)
    markup = await markup_crud.get_markup_by_dealer_price(dealer_price,
                                                          session)
    return paginate(markup)
