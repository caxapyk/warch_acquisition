import os
from flask import Flask, Blueprint, render_template
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
auth = HTTPBasicAuth()

bp_main = Blueprint('main', 'warch_acquisition.routes.main')


def create_app(config='warch_acquisition.config.Default'):
    app = Flask(__name__)
    app.config.from_object(config)

    # load configuration from settings.cfg
    basedir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), os.pardir))
    cfg_file = "%s/warch_acquisition/settings.cfg" % basedir
    if os.path.exists(cfg_file):
        app.config.from_pyfile(cfg_file)

    db.init_app(app)

    with app.app_context():
        from warch_acquisition.routes import main
        import warch_acquisition.context_processors
        import warch_acquisition.error
        import warch_acquisition.user
        
        app.register_blueprint(bp_main, url_prefix='/')

        return app
