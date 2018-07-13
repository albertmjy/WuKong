from .. import db


class FAQPage(db.Model):
    __tablename__ = 'faq_page'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(length=8), unique=True)
    answer = db.Column(db.Text(collation='utf8'))
    attachment = db.Column(db.text(collation='utf8'))

    @staticmethod
    def get_all_questions():
        return FAQPage.query.all()

    def __init__(self, question=None, answer=None, attachment=None):
        self.question = question
        self.answer = answer
        self.attachment = attachment

    def __repr__(self):
        return '<FAQ: %r>' % self.question
