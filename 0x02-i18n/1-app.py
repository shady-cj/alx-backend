#!/usr/bin/env python3
"""
Creating a simple web app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
class Config:
    LANGUAGES = ["en", "fr"]
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


@app.route('/', methods=['GET'])
def index():
    """
    Defining simple default route
    to return a template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5200)
