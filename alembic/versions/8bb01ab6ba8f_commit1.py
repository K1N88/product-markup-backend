"""commit1

Revision ID: 8bb01ab6ba8f
Revises: 
Create Date: 2023-11-29 23:47:01.601610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb01ab6ba8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dealer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('артикул товара', sa.String(length=100), nullable=False),
    sa.Column('код товара', sa.String(length=100), nullable=True),
    sa.Column('название товара', sa.String(length=1000), nullable=True),
    sa.Column('стоимость', sa.String(length=100), nullable=True),
    sa.Column('рекомендованная цена', sa.String(length=100), nullable=True),
    sa.Column('категория товара', sa.String(length=100), nullable=True),
    sa.Column('название товара на Озоне', sa.String(length=1000), nullable=True),
    sa.Column('название товара в 1C', sa.String(length=1000), nullable=True),
    sa.Column('название товара на Wildberries', sa.String(length=1000), nullable=True),
    sa.Column('описание для Озон', sa.String(length=100), nullable=True),
    sa.Column('артикул для Wildberries', sa.String(length=100), nullable=True),
    sa.Column('артикул для Wildberries td', sa.String(length=100), nullable=True),
    sa.Column('артикул для Яндекс.Маркета', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('артикул товара')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('dealerprice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_key', sa.String(length=1000), nullable=False),
    sa.Column('цена', sa.String(length=1000), nullable=False),
    sa.Column('адрес страницы, откуда собраны данные', sa.String(length=1000), nullable=True),
    sa.Column('заголовок продаваемого товара', sa.String(length=1000), nullable=False),
    sa.Column('дата получения информации', sa.Date(), nullable=False),
    sa.Column('dealer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['dealer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('markup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('дата рекомендации', sa.DateTime(), nullable=True),
    sa.Column('очередь', sa.Integer(), nullable=False),
    sa.Column('качество рекомендации', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['key'], ['dealerprice.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productdealerkey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('dealer_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dealer_id'], ['dealer.id'], ),
    sa.ForeignKeyConstraint(['key'], ['dealerprice.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('markup', sa.Integer(), nullable=True),
    sa.Column('дата обновления', sa.DateTime(), nullable=True),
    sa.Column('статус разметки', sa.Enum('YES', 'NO', 'HOLD', name='choice'), nullable=True),
    sa.ForeignKeyConstraint(['key'], ['dealerprice.id'], ),
    sa.ForeignKeyConstraint(['markup'], ['markup.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('statistic')
    op.drop_table('productdealerkey')
    op.drop_table('markup')
    op.drop_table('dealerprice')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('product')
    op.drop_table('dealer')
    # ### end Alembic commands ###