"""edit project model

Revision ID: 8525e79e1b56
Revises: c8cd1fc48b0b
Create Date: 2024-12-26 13:28:03.335666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8525e79e1b56'
down_revision: Union[str, None] = 'c8cd1fc48b0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('projects', 'contributors')



def downgrade() -> None:
    op.add_column('projects', sa.Column('contributors', sa.INTEGER(), autoincrement=False, nullable=False))

