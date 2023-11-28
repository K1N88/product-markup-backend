from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.dealer import dealerprise_crud
from app.core.db import get_async_session
from app.schemas.dealer import DealerPriceCreate
from app.core.user import current_user


router = APIRouter()


@router.get(
    '/',
    response_model=List[DealerPriceCreate],
    dependencies=[Depends(current_user)],
)
async def get_all_dealer_price(
    session: AsyncSession = Depends(get_async_session),
):
    dealer_price = await dealerprise_crud.get_multi(session)
    return dealer_price
  
