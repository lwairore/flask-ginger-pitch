from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_ow_four(error):
    return render_template('fourOwfour.html'), 404