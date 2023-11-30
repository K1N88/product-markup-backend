from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate

from app.core.db import get_async_session
from app.crud.product import product_crud
from app.schemas.product import ProductCreate, ProductDB
from app.core.user import current_user


router = APIRouter()


@router.post(
    "/",
    response_model=ProductDB,
    dependencies=[Depends(current_user)]
)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await product_crud.create(product_in, session)


@router.get(
    "/",
    response_model=Page[ProductDB],
    dependencies=[Depends(current_user)]
)
async def read_products(session: AsyncSession = Depends(get_async_session)):
    products = await product_crud.get_multi(session)
    return paginate(products)
