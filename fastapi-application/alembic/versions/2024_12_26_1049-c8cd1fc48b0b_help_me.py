"""help me

Revision ID: c8cd1fc48b0b
Revises: ddc7ff339ee9
Create Date: 2024-12-26 10:49:31.832024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8cd1fc48b0b'
down_revision: Union[str, None] = 'ddc7ff339ee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column('projects', sa.Column('name', sa.String(), nullable=False))
    op.add_column('projects', sa.Column('description', sa.Text(), nullable=False))
    op.add_column('projects', sa.Column('github_url', sa.String(), nullable=False))
    op.add_column('projects', sa.Column('contributors', sa.Integer(), nullable=False))
    op.drop_column('projects', 'Description')
    op.drop_column('projects', 'Name')
    op.drop_column('projects', 'Contributors')
    op.drop_column('projects', 'Github_URL')



def downgrade() -> None:

    op.add_column('projects', sa.Column('Github_URL', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('projects', sa.Column('Contributors', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('projects', sa.Column('Name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('projects', sa.Column('Description', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('projects', 'contributors')
    op.drop_column('projects', 'github_url')
    op.drop_column('projects', 'description')
    op.drop_column('projects', 'name')

