from fastapi import APIRouter

from app.api.endpoints.user import router as user_router
from app.api.endpoints.dealer import router as dealer_router
from app.api.endpoints.product import router as product_router
from app.api.endpoints.productdealerkey import router as productdealerkey_router
from app.api.endpoints.load_csv import router as load_csv_router
from app.api.endpoints.load_csv import router as load_csv_router


main_router = APIRouter()
main_router.include_router(user_router, tags=['users'])
main_router.include_router(dealer_router, prefix='/dealer', tags=['dealers'])
main_router.include_router(product_router, prefix='/product',
                           tags=['products'])
main_router.include_router(productdealerkey_router, prefix='/productdealerkey',
                           tags=['productdealerkeys'])
main_router.include_router(load_csv_router, prefix='/load_csv',
                           tags=['load_csv'])
