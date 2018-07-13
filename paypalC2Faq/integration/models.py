from .. import db


class Integration(db.Model):
    __tablename__ = 'integration_page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=8), unique=True)
    short_description = db.Column(db.Text(length=125, collation='utf8'), unique=True)
    description = db.Column(db.Text(collation='utf8'))
    attachment = db.Column(db.text(collation='utf8'))

    @staticmethod
    def get_all_pages():
        return Integration.query.all()

    def __init__(self, title=None, short_description=None, description=None, attachment=None):
        self.title = title
        self.short_description = short_description
        self.description = description
        self.attachment = attachment

    def __repr__(self):
        return '<Shopping Cart Page: %r>' % self.title


