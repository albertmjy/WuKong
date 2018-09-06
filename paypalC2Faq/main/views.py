from flask import render_template
from . import main

import requests
from bs4 import BeautifulSoup


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/address-generator')
def address_generator():
    dom = html_to_dom('https://faker.readthedocs.io/en/master/index.html')
    locale_links = dom.select('div#localization ul.simple > li > a.external.reference')
    country_locales = [locale_link.contents[0] for locale_link in locale_links]

    return render_template("address_generator.html", country_locales=country_locales)


def html_to_dom(url):
    # fetch the web page using requests
    response = requests.get(url)

    # represent page as BeautifoulSoup "soup" DOM object
    return BeautifulSoup(response.content, 'html.parser')