"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base  # noqa
from app.models.user import User  # noqa
from app.models.dealer import Dealer, DealerPrice  # noqa
from app.models.product import Product  # noqa
from app.models.productdealerkey import ProductDealerKey  # noqa
from app.models.markup import Markup, Statistic  # noqa
