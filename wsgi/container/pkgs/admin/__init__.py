import flask
import container.local.genshi as genshi
from flask import Blueprint, current_app, request, render_template
from container.local.genshi import Genshi, render_response
from genshi.template.loader import TemplateNotFound

bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates')


@bp.route("/")
def index():
    return genshi.render_response('base-layout.html')


@bp.route("/base-aside.html")
def aside():
    return render_response('base-aside.html', method='partial')
