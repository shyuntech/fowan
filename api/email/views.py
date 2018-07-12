from flask import Blueprint
from api.email import views

email = Blueprint('email', __name__, )