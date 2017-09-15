"""empty message

Revision ID: b0c57024a389
Revises: 46a7661bf550
Create Date: 2016-07-27 08:43:41.816902

"""

# revision identifiers, used by Alembic.
revision = 'b0c57024a389'
down_revision = '46a7661bf550'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('providers_comparison_google',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_identity', sa.Integer(), nullable=False),
    sa.Column('value', sa.BLOB(length=16000000), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_identity'], ['google_cloud_identity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('providers_comparison_google')
    ### end Alembic commands ###
