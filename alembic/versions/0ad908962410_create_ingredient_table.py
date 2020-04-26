"""create ingredient table

Revision ID: 0ad908962410
Revises: 7975c4f28c13
Create Date: 2020-04-26 16:27:46.809187

"""
from alembic import op
from sqlalchemy import Column, ForeignKey, Integer, String


# revision identifiers, used by Alembic.
revision = "0ad908962410"
down_revision = "7975c4f28c13"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ingredient",
        Column("id", Integer, primary_key=True),
        Column("value", String, nullable=False),
        Column("recipe_id", Integer, ForeignKey("recipe.id"), nullable=False),
    )


def downgrade():
    op.drop_table("ingredient")
