from fastapi import APIRouter

from app.api.endpoints.user import router as user_router
from app.api.endpoints.product import router as product_router


main_router = APIRouter()
main_router.include_router(user_router, prefix='/user', tags=['users'])
main_router.include_router(product_router, prefix='/product', tags=['products'])
