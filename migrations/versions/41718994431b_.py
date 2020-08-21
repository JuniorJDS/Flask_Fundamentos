"""empty message

Revision ID: 41718994431b
Revises: 0f8b4f6cb0f0
Create Date: 2020-08-13 21:24:49.760061

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '41718994431b'
down_revision = '0f8b4f6cb0f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clientes', 'andre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clientes', sa.Column('andre', mysql.VARCHAR(length=20), nullable=True))
    # ### end Alembic commands ###