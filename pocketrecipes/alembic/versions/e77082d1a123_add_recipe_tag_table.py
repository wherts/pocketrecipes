"""Add recipe tag table

Revision ID: e77082d1a123
Revises: 30a56eb98546
Create Date: 2020-05-10 10:24:08.928217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e77082d1a123"
down_revision = "30a56eb98546"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "recipe_tag",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipe.id"),
            nullable=False,
        ),
        sa.Column(
            "tag_id", sa.Integer(), sa.ForeignKey("tag.id"), nullable=False
        ),
    )


def downgrade():
    op.drop_table("recipe_tag")
