"""Top-level package for URL Shortner."""

__author__ = """Vaibhav Vikas"""
__email__ = 'vbhvvikas@gmail.com'
__version__ = '0.1.0'

from flask import Flask
from url_shortner.controller import user_controller

def create_app():
    app = Flask(__name__)
    app.debug = True

    @app.route("/", methods=["GET"])
    def status():
        return "App is running!"

    app.register_blueprint(user_controller.bp)

    return app
