"""add a middlename

Revision ID: b96053cd266f
Revises: 9158054509b5
Create Date: 2022-03-29 16:55:07.383305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b96053cd266f'
down_revision = '9158054509b5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('customer', sa.Column('middlename', sa.String(50)))

def downgrade():
    with op.batch_alter_table('customer') as batch_op:
        batch_op.drop_column('middlename')