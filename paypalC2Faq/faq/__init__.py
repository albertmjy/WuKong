from flask import Blueprint

faq_pages = Blueprint('faq_pages', __name__)

from . import views
