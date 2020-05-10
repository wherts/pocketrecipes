from pocketrecipes.db import db


class Instruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(), nullable=False)
    order = db.Column(db.Integer(), nullable=False)
    recipe_id = db.Column(
        db.Integer, db.ForeignKey("recipe.id"), nullable=False
    )

    def __repr__(self):
        return "Instruction: {order} - {text}".format(
            order=self.order, text=self.text
        )
