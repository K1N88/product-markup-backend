from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.base import CRUDBase
from app.models.product import Product
from app.crud.product import product_crud
from app.schemas.product import ProductCreate, ProductUpdate, ProductDB

router = APIRouter()


@router.post("/", response_model=ProductDB)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await product_crud.create(product_in, session)


@router.get("/", response_model=list[ProductDB])
async def read_products(
    session: AsyncSession = Depends(get_async_session),):
    return await product_crud.get_multi(session)