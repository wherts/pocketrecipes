from pocketrecipes.db import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    source_url = db.Column(db.Text())
    ingredients = db.relationship("Ingredient", backref="recipe")
    instructions = db.relationship("Instruction", backref="recipe")
    tags = db.relationship("RecipeTag", backref="recipe")

    def __repr__(self):
        return "Recipe: {title}".format(title=self.title)
