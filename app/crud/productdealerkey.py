from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.productdealerkey import ProductDealerKey
from app.models.product import Product
from app.models.dealer import Dealer



class CRUDProductDealerKey(CRUDBase):
    async def get_productdealerkey_by_ids(
            self, id: str, session: AsyncSession
        ) -> Optional[int]:
        db_productdealerkey_id = await session.execute(
            select(ProductDealerKey.id).where(ProductDealerKey.dealer_id == Dealer.id, ProductDealerKey.product_id == Product.id)
        )
        return db_productdealerkey_id.scalars().first()
    

productdealerkey_crud = CRUDProductDealerKey(ProductDealerKey)