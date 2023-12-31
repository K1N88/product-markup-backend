import csv
from datetime import datetime

from tqdm import tqdm
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser
from app.core.setup_logger import setup_logger
from app.models import Dealer, DealerPrice, Product


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

    with open('csv/marketing_dealer.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                id, name = row
                db_obj = Dealer(id=int(id), name=name)
                session.add(db_obj)
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {Dealer}', exc_info=True)
        await session.commit()
        message = f'количество объектов {Dealer} {count}'
        logger.info(message)
    result.append(message)

    with open('csv/marketing_dealerprice_dd.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                id, product_key, price, product_url, product_name, date, dealer_id = row
                db_obj = DealerPrice(
                    id=int(id),
                    product_key=product_key,
                    price=price,
                    product_url=product_url,
                    product_name=product_name,
                    date=datetime.strptime(date, '%Y-%m-%d'),
                    dealer_id=int(dealer_id),
                )
                session.add(db_obj)
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {DealerPrice}', exc_info=True)
        await session.commit()
        message = f'количество объектов {DealerPrice} {count}'
        logger.info(message)
    result.append(message)

    with open('csv/marketing_product.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        count = 0
        for row in tqdm(reader):
            try:
                num, id, article, ean_13, name, cost, recommended_price, category_id, ozon_name, name_1c, wb_name, ozon_article, wb_article, ym_article, wb_article_td = row
                db_obj = Product(
                    id=int(id),
                    article=article,
                    ean_13=ean_13,
                    name=name,
                    cost=cost,
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
                count += 1
            except Exception as error:
                logger.error(f'сбой {error} при сохранении {row} в модель {Product}', exc_info=True)
        await session.commit()
        message = f'количество объектов {Product} {count}'
        logger.info(message)
    result.append(message)

    return result
