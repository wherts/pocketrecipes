from pocketrecipes.db import db


class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer(), db.ForeignKey("tag.id"), nullable=False)
    recipe_id = db.Column(
        db.Integer(), db.ForeignKey("recipe.id"), nullable=False
    )

    def __repr__(self):
        return "Recipe Tag: {tag} for {recipe}".format(
            value=self.tag_id, recipe=self.recipe_id
        )
