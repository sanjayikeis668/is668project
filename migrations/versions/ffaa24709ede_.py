"""empty message

Revision ID: ffaa24709ede
Revises: ae587d288a2c
Create Date: 2021-04-20 18:34:26.112404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffaa24709ede'
down_revision = 'ae587d288a2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###
