from flask import Blueprint

bp = Blueprint('bootstrap', __name__, static_folder='static', template_folder='templates')
