"""create instruction table

Revision ID: 7cf3aef9a210
Revises: 0ad908962410
Create Date: 2020-04-26 16:45:01.296580

"""
from alembic import op
from sqlalchemy import Column, ForeignKey, Integer, String


# revision identifiers, used by Alembic.
revision = "7cf3aef9a210"
down_revision = "0ad908962410"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "recipe_instruction",
        Column("id", Integer, primary_key=True),
        Column("text", String, nullable=False),
        Column("order", Integer, nullable=False),
        Column("recipe_id", Integer, ForeignKey("recipe.id"), nullable=False),
    )


def downgrade():
    op.drop_table("recipe_instruction")
