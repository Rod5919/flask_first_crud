from flask import Blueprint, render_template
from controllers.user_controller import get_all_users

html_routes = Blueprint('html_routes', __name__)

# Home page
@html_routes.route('/')
def home():
    users = get_all_users()
    return render_template('index.html', users=users)