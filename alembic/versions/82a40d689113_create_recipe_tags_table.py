"""create recipe_tags table

Revision ID: 82a40d689113
Revises: 7b4f5ad574f1
Create Date: 2020-04-26 16:45:19.123904

"""
from alembic import op
from sqlalchemy import Column, ForeignKey, Integer, String


# revision identifiers, used by Alembic.
revision = "82a40d689113"
down_revision = "7b4f5ad574f1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "recipe_tags",
        Column("id", Integer, primary_key=True),
        Column("tag_id", Integer, ForeignKey("tag.id"), nullable=False),
        Column("recipe_id", Integer, ForeignKey("recipe.id"), nullable=False),
    )


def downgrade():
    op.drop_table("recipe_tags")
