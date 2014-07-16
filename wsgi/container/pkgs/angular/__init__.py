from flask import Blueprint

bp = Blueprint('angular', __name__, static_folder='static', template_folder='templates')
