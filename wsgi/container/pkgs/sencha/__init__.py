from flask import Blueprint

bp = Blueprint('sencha', __name__, static_folder='static', template_folder='templates')
