from pocketrecipes.db import db


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(200), nullable=False)
    recipe_id = db.Column(
        db.Integer, db.ForeignKey("recipe.id"), nullable=False
    )

    def __repr__(self):
        return "Ingredient: {value} {recipe}".format(
            value=self.value, recipe=self.recipe_id
        )
