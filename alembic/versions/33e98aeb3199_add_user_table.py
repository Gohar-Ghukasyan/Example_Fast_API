"""Add user table

Revision ID: 33e98aeb3199
Revises: a25a34309dd1
Create Date: 2022-09-11 13:57:17.211478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33e98aeb3199'
down_revision = 'a25a34309dd1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('Users')
