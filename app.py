from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from routes.main_routes import routes

from db.db import init_db

app = Flask(__name__)

# CORS
CORS(app)

# Init db
init_db(app)
app.register_blueprint(routes)