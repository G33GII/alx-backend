#!/usr/bin/env python3
"""
Flask app module that creates a simple route and
renders an HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index route that renders the 'index.html' template.

    Returns:
        str: Rendered HTML page content.
    """
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
