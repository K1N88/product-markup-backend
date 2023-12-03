from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


async def check_exists(
    id: int,
    session: AsyncSession,
    crud
):
    obj = await crud.get(id, session)
    if obj is None:
        raise HTTPException(
            status_code=404,
            detail=f'Объект модели {crud.model} не найден!'
        )
    return obj
