import csv

from tqdm import tqdm
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser
from app.core.setup_logger import setup_logger
from app.models import Dealer, DealerPrice, Product, ProductDealerKey


logger = setup_logger()

router = APIRouter()


@router.post(
    '/',
    response_model=List[str],
    dependencies=[Depends(current_superuser)],
)
async def load_csv(
    session: AsyncSession = Depends(get_async_session),
):
    logger.info('старт загрузки данных')
    result = []

    with open('csv/dealer.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                id, name = row
                db_obj = Dealer(id=id, name=name)
                session.add(db_obj)
                await session.commit()
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {Dealer}', exc_info=True)
        message = f'количество объектов {Dealer} {count}'
        logger.info(message)
    result.append(message)

    with open('csv/DealerPrice.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                product_key, price, product_url, product_name, date, dealer_id = row
                db_obj = DealerPrice(
                    product_key=product_key,
                    price=price,
                    product_url=product_url,
                    product_name=product_name,
                    date=date,
                    dealer_id=dealer_id,
                )
                session.add(db_obj)
                await session.commit()
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {DealerPrice}', exc_info=True)
        message = f'количество объектов {DealerPrice} {count}'
        logger.info(message)
    result.append(message)
    
    with open('csv/Product.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                article, ean_13, name, cost, min_recommended_price, recommended_price, category_id, ozon_name, name_1c, wb_name, ozon_article, wb_article, wb_article_td, ym_article = row
                db_obj = Product(
                    article=article,
                    ean_13=ean_13,
                    name=name,
                    cost=cost,
                    min_recommended_price=min_recommended_price,
                    recommended_price=recommended_price,
                    category_id=category_id,
                    ozon_name=ozon_name,
                    name_1c=name_1c,
                    wb_name=wb_name,
                    ozon_article=ozon_article,
                    wb_article=wb_article,
                    wb_article_td=wb_article_td,
                    ym_article=ym_article
                )
                session.add(db_obj)
                await session.commit()
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {Product}', exc_info=True)
        message = f'количество объектов {Product} {count}'
        logger.info(message)
    result.append(message)

    with open('csv/ProductDealerKey.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                key, dealer_id, product_id = row
                db_obj = ProductDealerKey(
                    key=key,
                    dealer_id=dealer_id,
                    product_id=product_id,
                )
                session.add(db_obj)
                await session.commit()
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {ProductDealerKey}', exc_info=True)
        message = f'количество объектов {ProductDealerKey} {count}'
        logger.info(message)
    result.append(message)

    return result
