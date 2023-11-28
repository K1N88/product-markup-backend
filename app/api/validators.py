from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.dealer import dealer_crud
from app.models import Dealer


async def check_dealer_exists(
    dealer_id: int,
    session: AsyncSession,
) -> Dealer:
    dealer = await dealer_crud .get(dealer_id, session)
    if dealer is None:
        raise HTTPException(
            status_code=404,
            detail='Дилер не найден!'
        )
    return dealer
