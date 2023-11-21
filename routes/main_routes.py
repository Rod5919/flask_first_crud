from flask import Blueprint

from .user_routes import user_routes
from .html_routes import html_routes

routes = Blueprint('routes', __name__)

# Register all routes
routes.register_blueprint(user_routes, url_prefix='/user')
routes.register_blueprint(html_routes, url_prefix='/')