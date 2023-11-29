from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.dealer import dealer_crud
from app.models import Dealer, DealerPrice


async def check_dealer_exists(
    dealer_id: int,
    session: AsyncSession,
) -> Dealer:
    dealer = await dealer_crud.get(dealer_id, session)
    if dealer is None:
        raise HTTPException(
            status_code=404,
            detail='Дилер не найден!'
        )
    return dealer


async def check_dealer_price_exists(
    dealer_price_id: int,
    session: AsyncSession,
) -> DealerPrice:
    dealer_price = await dealerprice_crud.get(dealer_price_id, session)
    if dealer_price is None:
        raise HTTPException(
            status_code=404,
            detail='Товар не найден!'
        )
    return dealer_price
