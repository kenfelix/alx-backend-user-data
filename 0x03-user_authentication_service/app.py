#!/usr/bin/env python3
"""
Flask app Module
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def basic() -> str:


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")