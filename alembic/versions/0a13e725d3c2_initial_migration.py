"""Initial migration

Revision ID: 0a13e725d3c2
Revises: 2b4e8fa0ef72
Create Date: 2024-06-18 15:12:41.511308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a13e725d3c2'
down_revision: Union[str, None] = '2b4e8fa0ef72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###