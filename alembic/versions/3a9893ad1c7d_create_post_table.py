"""create post table

Revision ID: 3a9893ad1c7d
Revises: 
Create Date: 2022-09-11 13:23:30.542405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a9893ad1c7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))


def downgrade():
    op.drop_table('Posts')
