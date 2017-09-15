"""empty message

Revision ID: 7ed30ae8f391
Revises: a1dc4d972c6b
Create Date: 2017-04-04 11:49:17.109112

"""

# revision identifiers, used by Alembic.
revision = '7ed30ae8f391'
down_revision = 'a1dc4d972c6b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('aws_key', sa.Column('is_valid_key', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('aws_key', 'is_valid_key')
    ### end Alembic commands ###
