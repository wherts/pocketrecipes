from flask_sqlalchemy import SQLAlchemy
from pocketrecipes.app import app

db = SQLAlchemy(app)
