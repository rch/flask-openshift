from flask import Blueprint

bp = Blueprint('common', __name__, static_folder='static', template_folder='templates')

@bp.route("/ping/")
@bp.route("/ping/<int:a>/")
@bp.route("/ping/<int:a>/<int:b>/")
def ping(a=0, b=0):
    val = add_together(a, b)
    return render_template('ping.html', msg=val)
