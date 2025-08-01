"""update questions data

Revision ID: 7643f9ac6876
Revises: 386fb4c779c3
Create Date: 2025-08-01 14:22:48.144138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7643f9ac6876'
down_revision: Union[str, Sequence[str], None] = '386fb4c779c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
