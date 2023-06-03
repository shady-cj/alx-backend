#!/usr/bin/env python3
"""
Creating a simple web app
with internationalization
"""
from flask_babel import Babel, format_datetime
import datetime
from flask import Flask, request, g, render_template
import pytz


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
    user = getattr(g, 'user', None)
    if user is not None and user.get('locale') in Config.LANGUAGES:
        return user.get('locale')
    header_locale = request.headers.get('locale')
    if header_locale is not None and header_locale in Config.LANGUAGES:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    returning the best matching
    timezone
    """
    try:
        timezone = request.args.get('timezone')
        if timezone is not None:
            pytz_zone = pytz.timezone(timezone)
            return pytz_zone.zone
        user = getattr(g, "user", None)
        if user is not None:
            pytz_zone = pytz.timezone(user.get('timezone'))
            return pytz_zone.zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]

@app.route('/', methods=['GET'])
def index():
    """
    Defining simple default route
    to return a template
    """
    return render_template('index.html', user=getattr(g, 'user', None), time=g.time)


@app.before_request
def before_request():
    """
    Executes before all request
    """
    user = get_user()
    if user is not None:
        g.user = user
    g.time = format_datetime(datetime.datetime.now())


if __name__ == '__main__':
    app.run(port=5200)
