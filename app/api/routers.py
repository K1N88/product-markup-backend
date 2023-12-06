from fastapi import APIRouter

from app.api.endpoints.user import router as user_router
from app.api.endpoints.dealer import router as dealer_router
from app.api.endpoints.dealerprice import router as dealerprice_router
from app.api.endpoints.product import router as product_router
from app.api.endpoints.productdealerkey import router as productdealer_router
from app.api.endpoints.load_csv import router as load_csv_router
from app.api.endpoints.markup import router as markup_router
from app.api.endpoints.statistic import router as statistic_router


main_router = APIRouter()

main_router.include_router(dealer_router, prefix='/dealer', tags=['dealers'])
main_router.include_router(product_router, prefix='/product',
                           tags=['products'])
main_router.include_router(productdealer_router, prefix='/productdealerkey',
                           tags=['productdealerkeys'])
main_router.include_router(load_csv_router, prefix='/load_csv',
                           tags=['load_csv'])
main_router.include_router(dealerprice_router, prefix='/dealerprice',
                           tags=['dealerprice'])
main_router.include_router(markup_router, prefix='/markup', tags=['markup'])
main_router.include_router(statistic_router, prefix='/statistic',
                           tags=['statistic'])
