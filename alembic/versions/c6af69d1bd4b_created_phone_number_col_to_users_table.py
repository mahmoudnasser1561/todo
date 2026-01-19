"""Created phone_number col to Users Table

Revision ID: c6af69d1bd4b
Revises: 
Create Date: 2026-01-19 16:53:01.561044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6af69d1bd4b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

def downgrade():
    op.drop_column('users', 'phone_number')
