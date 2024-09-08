#!/usr/bin/env python3
"""
Task 0: Basic Flask app with Babel for localization.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask-Babel.
    
    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default language for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Default route that renders the homepage.

    Returns:
        str: Rendered HTML page content.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
