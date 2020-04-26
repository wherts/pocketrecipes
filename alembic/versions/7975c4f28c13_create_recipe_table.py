"""create recipe table

Revision ID: 7975c4f28c13
Revises: 
Create Date: 2020-04-26 16:12:00.326820

"""
from alembic import op
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision = "7975c4f28c13"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "recipe",
        Column("id", Integer, primary_key=True),
        Column("title", String, nullable=False),
        Column("source_url", String, nullable=False),
    )


def downgrade():
    op.drop_table("recipe")
