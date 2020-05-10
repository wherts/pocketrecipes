"""Add instruction table

Revision ID: f4ba65070ecd
Revises: 00aea3abce57
Create Date: 2020-05-10 10:23:57.546841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f4ba65070ecd"
down_revision = "00aea3abce57"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "instruction",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipe.id"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("instruction")
