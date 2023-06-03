#!/usr/bin/env python3
"""
Creating a simple web app
with internationalization
"""
from flask_babel import Babel
from flask import Flask, request, g, render_template


app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
     returns a user dictionary or None if the ID cannot be found
     or if login_as was not passed.
    """
    login_as = request.args.get('login_as')
    if login_as is not None:
        return users.get(int(login_as))
    return login_as


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
    return render_template('5-index.html', user=getattr(g, 'user', None))


@app.before_request
def before_request():
    """
    Executes before all request
    """
    user = get_user()
    if user is not None:
        g.user = user


if __name__ == '__main__':
    app.run(port=5200)
