"""create tag table

Revision ID: 7b4f5ad574f1
Revises: 7cf3aef9a210
Create Date: 2020-04-26 16:45:09.724869

"""
from alembic import op
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision = "7b4f5ad574f1"
down_revision = "7cf3aef9a210"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tag",
        Column("id", Integer, primary_key=True),
        Column("name", String, nullable=False),
    )


def downgrade():
    op.drop_table("tag")
