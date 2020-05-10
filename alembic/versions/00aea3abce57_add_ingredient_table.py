"""Add ingredient table

Revision ID: 00aea3abce57
Revises: 4f2d4a3bb352
Create Date: 2020-05-10 10:06:35.535655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "00aea3abce57"
down_revision = "4f2d4a3bb352"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ingredient",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("value", sa.String(length=200), nullable=False),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipe.id"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("ingredient")
