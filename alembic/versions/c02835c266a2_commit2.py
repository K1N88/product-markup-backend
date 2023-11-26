"""commit2

Revision ID: c02835c266a2
Revises: bddc6c82011c
Create Date: 2023-11-26 19:20:30.017765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02835c266a2'
down_revision = 'bddc6c82011c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dealerprice', sa.Column('адрес страницы, откуда собраны данные', sa.String(length=1000), nullable=True))
    op.drop_column('dealerprice', 'адрес страницы, откуда собраны дан')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dealerprice', sa.Column('адрес страницы, откуда собраны дан', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.drop_column('dealerprice', 'адрес страницы, откуда собраны данные')
    # ### end Alembic commands ###
