from flask import Blueprint


# Defining our Blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h1>Test </h1>'