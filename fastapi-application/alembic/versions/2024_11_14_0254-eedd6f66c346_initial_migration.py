"""Initial migration

Revision ID: eedd6f66c346
Revises: 
Create Date: 2024-11-14 02:54:49.253626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eedd6f66c346'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('foo', sa.Integer(), nullable=False),
    sa.Column('bar', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('foo', 'bar', name=op.f('uq_users_foo_bar')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )



def downgrade() -> None:
    op.drop_table('users')
