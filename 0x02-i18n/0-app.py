#!/usr/bin/env python3
"""
Creating a simple web app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Defining simple default route
    to return a template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5200)