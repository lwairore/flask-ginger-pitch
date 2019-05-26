from flask import Flask


def create_app(config_name):
    app = Flask(__name__)