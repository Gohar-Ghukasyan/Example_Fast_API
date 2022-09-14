"""Add last few columns to Posts table

Revision ID: 26d619f547b7
Revises: cc77d0ac140e
Create Date: 2022-09-11 14:22:55.864513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d619f547b7'
down_revision = 'cc77d0ac140e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('Posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                                     nullable=False))


def downgrade():
    op.drop_column('Posts', 'published')
    op.drop_column('Posts', 'created_at')
