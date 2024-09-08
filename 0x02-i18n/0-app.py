#!/usr/bin/env python3
"""
Flask app module that creates a simple route and renders an HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Index route that renders the 'index.html' template.

    Returns:
        str: Rendered HTML page content.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
