from flask import render_template
from . import shopping_cart_pages

from .models import ShoppingCartPage


@shopping_cart_pages('/shopping_cart')
def shopping_cart():

    all_pages = ShoppingCartPage.get_all_pages()
    return render_template('shopping_cart/main.html', all_shopping_cart_pages=all_pages)


