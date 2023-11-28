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
