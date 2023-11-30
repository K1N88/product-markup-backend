from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate

from app.crud.dealer import dealerprice_crud
from app.core.db import get_async_session
from app.schemas.dealer import DealerPriceDB
from app.core.user import current_user
from app.api.validators import check_dealer_exists


router = APIRouter()


@router.get(
    '/',
    response_model=Page[DealerPriceDB],
    dependencies=[Depends(current_user)]
)
async def get_all_dealer_price(
    session: AsyncSession = Depends(get_async_session)
):
    dealer_price = await dealerprice_crud.get_multi(session)
    return paginate(dealer_price)


@router.get(
    '/{dealer_id}',
    response_model=Page[DealerPriceDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)]
)
async def get_dealer_price(
    dealer_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    dealer = await check_dealer_exists(dealer_id, session)
    prices = await dealerprice_crud.get_all_products_by_dealer(dealer, session)
    return paginate(prices)
