"""empty message

Revision ID: 3a20ee4b2ae6
Revises: 182aedb166ea
Create Date: 2021-04-27 14:52:12.402954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a20ee4b2ae6'
down_revision = '182aedb166ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assignments', sa.Column('classname', sa.String(length=4096), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assignments', 'classname')
    # ### end Alembic commands ###
