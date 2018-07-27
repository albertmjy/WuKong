from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate


from .config import config_by_name

db = SQLAlchemy()
migrate = Migrate()

toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .faq import faq_pages as faq_pages_blueprint
    app.register_blueprint(faq_pages_blueprint, url_prefix='/faq')

    from .integration import integration_pages as integration_pages_blueprint
    app.register_blueprint(integration_pages_blueprint, url_prefix='/integration')

    from .shopping_cart import shopping_cart_pages as shopping_cart_pages_blueprint
    app.register_blueprint(shopping_cart_pages_blueprint, url_prefix='/shopping-cart')

    return app

