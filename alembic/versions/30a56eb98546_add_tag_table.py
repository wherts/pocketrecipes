"""Add tag table

Revision ID: 30a56eb98546
Revises: f4ba65070ecd
Create Date: 2020-05-10 10:24:04.325693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30a56eb98546"
down_revision = "f4ba65070ecd"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(100), unique=True, nullable=False),
    )


def downgrade():
    op.drop_table("tag")
