import pkgs
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
    app.register_blueprint(pkgs.admin.bp, url_prefix='/admin')
    app.register_blueprint(pkgs.angular.bp, url_prefix='/angular')
    app.register_blueprint(pkgs.common.bp, url_prefix='/common')
    app.register_blueprint(pkgs.bootstrap.bp, url_prefix='/bootstrap')
    app.register_blueprint(pkgs.ngstrap.bp, url_prefix='/ngstrap')
