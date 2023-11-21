from flask_sqlalchemy import SQLAlchemy
from config.config import database_uri
db = SQLAlchemy()

from models import *

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()