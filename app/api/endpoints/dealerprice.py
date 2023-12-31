from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate

from app.crud.dealer import dealerprice_crud, dealer_crud
from app.core.db import get_async_session
from app.schemas.dealer import DealerPriceDealerDB
from app.core.user import current_user
from app.api.validators import check_exists


router = APIRouter()


@router.get(
    '/',
    response_model=Page[DealerPriceDealerDB],
    dependencies=[Depends(current_user)]
)
async def get_all_dealer_price(
    session: AsyncSession = Depends(get_async_session),
    name: Optional[str] = None,
    state: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
):
    prices = await dealerprice_crud.get_multi_products(
        session, name=name, state=state, start_date=start_date,
        end_date=end_date
    )
    return paginate(prices)


@router.get(
    '/{dealer_id}',
    response_model=Page[DealerPriceDealerDB],
    response_model_exclude_none=False,
    dependencies=[Depends(current_user)]
)
async def get_dealer_price(
    dealer_id: int,
    name: Optional[str] = None,
    state: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    session: AsyncSession = Depends(get_async_session)
):
    dealer = await check_exists(dealer_id, session, dealer_crud)
    prices = await dealerprice_crud.get_all_products_by_dealer(
        dealer, session, name=name, state=state, start_date=start_date,
        end_date=end_date
    )
    return paginate(prices)
