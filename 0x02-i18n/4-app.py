#!/usr/bin/env python3
"""
Creating a simple web app
with internationalization
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    babel configs
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    returning the best language match.
    """
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.\
        best_match(app.config["LANGUAGES"])


@app.route('/', methods=['GET'])
def index():
    """
    Defining simple default route
    to return a template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port=5200)
