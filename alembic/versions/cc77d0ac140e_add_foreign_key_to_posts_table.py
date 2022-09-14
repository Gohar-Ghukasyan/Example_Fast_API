"""add foreign-key to Posts table

Revision ID: cc77d0ac140e
Revises: 33e98aeb3199
Create Date: 2022-09-11 14:12:30.994367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc77d0ac140e'
down_revision = '33e98aeb3199'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='Posts', referent_table='Users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_users_fk', table_name='Posts')
    op.drop_column('Posts', 'owner_id')
