"""Add recipe table

Revision ID: 4f2d4a3bb352
Revises:
Create Date: 2020-05-10 09:56:43.969242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4f2d4a3bb352"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "recipe",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=True),
        sa.Column("source_url", sa.Text(), nullable=True),
    )


def downgrade():
    op.drop_table("recipe")
