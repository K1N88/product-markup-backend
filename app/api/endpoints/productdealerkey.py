from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page, paginate

from app.core.db import get_async_session
from app.crud.productdealerkey import productdealerkey_crud
from app.schemas.productdealerkey import (ProductDealerKeyCreate,
                                          ProductDealerKeyDB)
from app.core.user import current_user
from app.api.validators import check_exists


router = APIRouter()


@router.post("/", response_model=ProductDealerKeyDB,
             dependencies=[Depends(current_user)])
async def create_productdealerkey(
    product_in: ProductDealerKeyCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await productdealerkey_crud.create(product_in, session)


@router.get("/", response_model=Page[ProductDealerKeyDB],
            dependencies=[Depends(current_user)])
async def read_productdealerkey(
    session: AsyncSession = Depends(get_async_session)
):
    productdealerkey = await productdealerkey_crud.get_multi(session)
    return paginate(productdealerkey)


@router.patch('/{productdealerkey_id}', response_model=ProductDealerKeyDB,
              dependencies=[Depends(current_user)])
async def update_productdealerkey(
        productdealerkey_id: int,
        obj_in: ProductDealerKeyCreate,
        session: AsyncSession = Depends(get_async_session),
):
    productdealerkey = await check_exists(
        productdealerkey_id, session, productdealerkey_crud
    )
    productdealerkey = await productdealerkey_crud.update(
        db_obj=productdealerkey,
        obj_in=obj_in,
        session=session,
    )
    return productdealerkey


@router.delete('/{productdealerkey_id}', response_model=ProductDealerKeyDB,
               dependencies=[Depends(current_user)])
async def delete_productdealerkey(
        productdealerkey_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    productdealerkey = await check_exists(
        productdealerkey_id, session, productdealerkey_crud
    )
    productdealerkey = await productdealerkey_crud.remove(productdealerkey,
                                                          session)
    return productdealerkey
