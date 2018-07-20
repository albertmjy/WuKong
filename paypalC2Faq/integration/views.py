from flask import render_template
from . import integration_pages
from ..models import IntegrationPage


@integration_pages.route('/')
def index():
    return render_template('integration/main.html')


@integration_pages.route('/step')
def step():
    return render_template('integration/step.html')