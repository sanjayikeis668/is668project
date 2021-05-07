"""empty message

Revision ID: 6f549d2f6804
Revises: 00be1a802765
Create Date: 2021-04-20 19:26:52.249634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f549d2f6804'
down_revision = '00be1a802765'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commenter_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['commenter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'commenter_id')
    # ### end Alembic commands ###
