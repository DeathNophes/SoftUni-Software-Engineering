"""Relation

Revision ID: 43f1de36423a
Revises: 759460ae112f
Create Date: 2024-08-15 18:48:28.983578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43f1de36423a'
down_revision: Union[str, None] = '759460ae112f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employees', 'cities', ['city_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.drop_column('employees', 'city_id')
    # ### end Alembic commands ###
