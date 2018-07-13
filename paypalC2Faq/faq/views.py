from flask import render_template
from . import faq_pages
from .models import FAQPage


@faq_pages.route('/faq')
def faq():

    all_faqs = FAQPage.get_all_questions()
    return render_template('faq/main.html', all_faqs=all_faqs)