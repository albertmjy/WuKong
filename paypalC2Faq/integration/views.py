from flask import render_template
from . import integration_pages


@integration_pages.route('/integration')
def integration():
    return render_template('integration/main.html')


@integration_pages.route('/step')
def step():
    return render_template('integration/step.html')