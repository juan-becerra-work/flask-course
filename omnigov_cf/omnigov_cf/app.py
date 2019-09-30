from flask import Flask

from omnigov_cf.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """

    # Says to Flask to find the "instance" module
    #    in the same folder than the main module
    app = Flask(__name__, instance_relative_config=True)

    # It loads the settings.py file from the "config" module
    #    where config variables are defined
    app.config.from_object('config.settings')

    # It loads the settings.py file from the "instance" module
    #    where config variables are defined for PRODUCTION
    # It overrides the previous line, if setting.py exists
    # It must be excluded from version control
    # silent=True says to Flask not to crash if file doesn't exists
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    return app
