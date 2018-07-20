from . import db


class FAQPage(db.Model):
    __tablename__ = 'faq_page'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(length=8), unique=True)
    answer = db.Column(db.Text())
    attachment = db.Column(db.Text())

    @staticmethod
    def get_all_questions():
        return FAQPage.query.all()

    def __init__(self, question=None, answer=None, attachment=None):
        self.question = question
        self.answer = answer
        self.attachment = attachment

    def __repr__(self):
        return '<FAQ: %r>' % self.question


class IntegrationPage(db.Model):
    __tablename__ = 'integration_page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=8), unique=True)
    short_description = db.Column(db.Text(length=125), unique=True)
    description = db.Column(db.Text())
    attachment = db.Column(db.Text())

    @staticmethod
    def get_all_pages():
        return IntegrationPage.query.all()

    def __init__(self, title=None, short_description=None, description=None, attachment=None):
        self.title = title
        self.short_description = short_description
        self.description = description
        self.attachment = attachment

    def __repr__(self):
        return '<Shopping Cart Page: %r>' % self.title


class ShoppingCartPage(db.Model):
    __tablename__ = 'shopping_cart_page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=8), unique=True)
    short_description = db.Column(db.Text(length=125), unique=True)
    description = db.Column(db.Text())
    attachment = db.Column(db.Text())

    @staticmethod
    def get_all_pages():
        return ShoppingCartPage.query.all()

    def __init__(self, title=None, short_description=None, description=None, attachment=None):
        self.title = title
        self.short_description = short_description
        self.description = description
        self.attachment = attachment

    def __repr__(self):
        return '<Shopping Cart Page: %r>' % self.title
