"""Add User field rol_id

Revision ID: 2e2446020757
Revises: c66a108b0c33
Create Date: 2022-04-27 22:47:36.683125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2446020757'
down_revision = 'c66a108b0c33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rol_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rol_id')
    # ### end Alembic commands ###