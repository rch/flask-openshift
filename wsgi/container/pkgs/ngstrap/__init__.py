from flask import Blueprint

bp = Blueprint('ngstrap', __name__, static_folder='static', template_folder='templates')
