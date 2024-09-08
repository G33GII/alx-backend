#!/usr/bin/env python3
"""
Task 2: Get locale from request with Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask-Babel.

    Attributes:
        DEBUG (bool): Enables debug mode for the Flask app.
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the best-matching locale from the request headers.

    Returns:
        str: The best-matching language for the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Default route that renders the homepage.

    Returns:
        str: Rendered HTML page content.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
