"""Remove test model

Revision ID: 9eb03eb0f76f
Revises: 48e4e7786f07
Create Date: 2022-04-27 21:20:28.362912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9eb03eb0f76f'
down_revision = '48e4e7786f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_migration')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_migration',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='test_migration_pkey')
    )
    # ### end Alembic commands ###