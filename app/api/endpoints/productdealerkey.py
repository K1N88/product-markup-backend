from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.productdealerkey import productdealerkey_crud
from app.schemas.productdealerkey import (ProductDealerKeyCreate,
                                          ProductDealerKeyDB)


router = APIRouter()


@router.post("/", response_model=ProductDealerKeyDB)
async def create_product(
    product_in: ProductDealerKeyCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await productdealerkey_crud.create(product_in, session)


@router.get("/", response_model=list[ProductDealerKeyDB])
async def read_products(session: AsyncSession = Depends(get_async_session),):
    return await productdealerkey_crud.get_multi(session)
