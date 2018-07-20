from flask import Blueprint


shopping_cart_pages = Blueprint('shopping_cart_pages', __name__)


from . import views
