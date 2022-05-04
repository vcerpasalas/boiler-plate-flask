"""add fields authentication

Revision ID: a03486f79472
Revises: 993706a50742
Create Date: 2022-04-28 22:28:12.725494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03486f79472'
down_revision = '993706a50742'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=80), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
