import flask
from celery import Celery
import sqlite3.dbapi2 as sqlite3


def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


def register_blueprints(app, mapping=None):
    import pkgs
    app.register_blueprint(pkgs.admin.bp, url_prefix='/admin')
    app.register_blueprint(pkgs.angular.bp, url_prefix='/angular')
    app.register_blueprint(pkgs.common.bp, url_prefix='/common')
    app.register_blueprint(pkgs.bootstrap.bp, url_prefix='/bootstrap')
    app.register_blueprint(pkgs.ngstrap.bp, url_prefix='/ngstrap')


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(flask.current_app.config['ADMINDB'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with flask.current_app.open_resource('admin.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = connect_db()
    return flask.g.sqlite_db

