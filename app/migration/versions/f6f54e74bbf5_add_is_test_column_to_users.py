"""Add is_test column to users

Revision ID: f6f54e74bbf5
Revises: 0a59332ab770
Create Date: 2024-11-04 14:21:34.214936

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6f54e74bbf5'
down_revision: Union[str, None] = '0a59332ab770'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('is_test', sa.Boolean(), server_default=sa.text('(false)'), nullable=False))
    op.add_column('users', sa.Column('is_test', sa.Boolean(), server_default=sa.text('(false)'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_test')
    op.drop_column('messages', 'is_test')
    # ### end Alembic commands ###
