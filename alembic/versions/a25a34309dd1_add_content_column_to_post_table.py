"""add content column to post table

Revision ID: a25a34309dd1
Revises: 3a9893ad1c7d
Create Date: 2022-09-11 13:47:46.815048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a25a34309dd1'
down_revision = '3a9893ad1c7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('Posts', 'content')
