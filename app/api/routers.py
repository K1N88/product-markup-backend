from fastapi import APIRouter

from app.api.endpoints.user import router as user_router
from app.api.endpoints.dealer import router as dealer_router
from app.api.endpoints.dealerprice import router as dealerprice_router
from app.api.endpoints.product import router as product_router
from app.api.endpoints.productdealerkey import router as productdealerkey_router
from app.api.endpoints.load_csv import router as load_csv_router
from app.api.endpoints.markup import router as markup_router


main_router = APIRouter()
main_router.include_router(user_router, tags=['users'])
main_router.include_router(dealer_router, prefix='/dealer', tags=['dealer'])
main_router.include_router(dealer_router, prefix='/dealerprice', tags=['dealerprice'])
main_router.include_router(product_router, prefix='/product', tags=['product'])
main_router.include_router(productdealerkey_router, prefix='/productdealerkey', tags=['productdealerkey'])
main_router.include_router(load_csv_router, prefix='/load_csv', tags=['load_csv'])
main_router.include_router(markup_router, prefix='/', tags=['markup'])
