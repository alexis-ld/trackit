"""empty message

Revision ID: fd62ceaa257c
Revises: b6a1dba48f9a
Create Date: 2016-06-01 02:10:19.403490

"""

# revision identifiers, used by Alembic.
revision = 'fd62ceaa257c'
down_revision = 'b6a1dba48f9a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('google_cloud_billing_file', 'bucket')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('google_cloud_billing_file', sa.Column('bucket', mysql.VARCHAR(length=224), nullable=False))
    ### end Alembic commands ###
