import factory.alchemy
from .. import db
from ..models import ShoppingCartPage


class ShoppingCartPageFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ShoppingCartPage
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    title = factory.Faker('sentence', locale='zh_CN', nb_words=4)
    short_description = factory.Faker('paragraph', locale='zh_CN', nb_sentences=3, ext_word_list=None)
    description = factory.Faker('text', locale='zh_CN', max_nb_chars=600, ext_word_list=None)
    attachment = factory.Faker('file_name', locale='zh_CN', category=None, extension='PDF')
