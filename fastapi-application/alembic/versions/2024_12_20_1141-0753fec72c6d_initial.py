"""initial

Revision ID: 0753fec72c6d
Revises: 
Create Date: 2024-12-20 11:41:44.856636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0753fec72c6d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=False),
    sa.Column('Disctiption', sa.Text(), nullable=False),
    sa.Column('Github_Url', sa.String(), nullable=False),
    sa.Column('Contributors', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_projects')),
    sa.UniqueConstraint('Name', name=op.f('uq_projects_Name'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )



def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('projects')
