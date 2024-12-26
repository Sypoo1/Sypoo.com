"""fix spelling

Revision ID: ddc7ff339ee9
Revises: 6c7d443abd8b
Create Date: 2024-12-26 10:37:03.757881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddc7ff339ee9'
down_revision: Union[str, None] = '6c7d443abd8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('uq_projects_Name', 'projects', type_='unique')


def downgrade() -> None:
    op.create_unique_constraint('uq_projects_Name', 'projects', ['Name'])
