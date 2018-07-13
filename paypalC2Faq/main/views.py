from flask import render_template
from . import home_page


@home_page.route('/')
def index():
    return render_template("index.html")
