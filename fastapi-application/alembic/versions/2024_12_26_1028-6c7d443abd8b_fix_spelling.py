"""fix spelling

Revision ID: 6c7d443abd8b
Revises: 0753fec72c6d
Create Date: 2024-12-26 10:28:27.983241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7d443abd8b'
down_revision: Union[str, None] = '0753fec72c6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('projects', sa.Column('Description', sa.Text(), nullable=False))
    op.add_column('projects', sa.Column('Github_URL', sa.String(), nullable=False))
    op.drop_column('projects', 'Disctiption')
    op.drop_column('projects', 'Github_Url')


def downgrade() -> None:
    op.add_column('projects', sa.Column('Github_Url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('projects', sa.Column('Disctiption', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('projects', 'Github_URL')
    op.drop_column('projects', 'Description')
