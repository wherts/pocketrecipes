from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = "prod"

if ENV == "dev":
    app.debug = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://wesleyherts:12345@localhost/lexus"
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgres://ivzsszehsnajzh:"
        + "b1de725ca318ff69cc600586d81988296450a097711bc3d52485416a8b69a032"
        + "@ec2-52-71-55-81.compute-1.amazonaws.com:5432/d6823qnacdvbos"
    )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comment):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comment = comment


@app.route("/")
def index():
    return render_template("naz.html")


@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        customer = request.form["customer"]
        dealer = request.form["dealer"]
        rating = request.form["rating"]
        comments = request.form["comments"]
        if not customer or not dealer:
            return render_template(
                "index.html", message="Please enter required fields"
            )

        if (
            not db.session.query(Feedback)
            .filter(Feedback.customer == customer)
            .count()
        ):
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()

            return render_template("success.html")
        return render_template(
            "index.html", message="You have already submitted feedback"
        )


if __name__ == "__main__":
    app.run()
