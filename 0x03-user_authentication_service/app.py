#!/usr/bin/env python3
"""
Flask app Module
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def basic() -> str:
    """
    returns a basic json response
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def  users() -> str:
    """register a new user"""
    email = request.form.get("email")
    password = request.form.get("password")
    
    try:
        user = AUTH.register_user(email, password)
        if user is not None:
            return jsonify({
                "email": user.email,
                "message": "user created"
                })
    except ValueError:
        return jsonify({
            "message": "email already registered"
            }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
