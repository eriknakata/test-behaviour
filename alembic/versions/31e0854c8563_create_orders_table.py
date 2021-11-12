"""create orders table

Revision ID: 31e0854c8563
Revises: 
Create Date: 2021-11-10 21:36:49.878543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31e0854c8563'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('created_at', sa.DateTime(), default=sa.func.now(), nullable=False),
        sa.Column('customer_email', sa.String(), nullable=False),
        sa.Column('total', sa.DECIMAL(), nullable=False))


def downgrade():
    op.drop_table('orders')
