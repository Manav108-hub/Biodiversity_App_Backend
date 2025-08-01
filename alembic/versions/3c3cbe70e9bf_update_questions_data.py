"""update questions data

Revision ID: 3c3cbe70e9bf
Revises: 7643f9ac6876
Create Date: 2025-08-01 14:23:21.223934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c3cbe70e9bf'
down_revision: Union[str, Sequence[str], None] = '7643f9ac6876'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
