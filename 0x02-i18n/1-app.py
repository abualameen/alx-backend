#!/usr/bin/env python3
"""
this module implement Babel

"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ this class difines the bebel settings"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """this is the index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', poty=5000)
