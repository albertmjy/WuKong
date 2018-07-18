from flask import Blueprint


integration_pages = Blueprint('integration_pages', __name__)

from . import views
