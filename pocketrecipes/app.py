from flask import Flask, render_template, request

import engine

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    app.debug = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://wesleyherts:12345@localhost/pocketrecipes"
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgres://ivzsszehsnajzh:"
        + "b1de725ca318ff69cc600586d81988296450a097711bc3d52485416a8b69a032"
        + "@ec2-52-71-55-81.compute-1.amazonaws.com:5432/d6823qnacdvbos"
    )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    recipe_title = engine.scrape_recipe(request.form["recipe_source"])
    return render_template("index.html", message=recipe_title)


if __name__ == "__main__":
    app.run()
