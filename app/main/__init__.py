from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, forms, errors, edit_config
