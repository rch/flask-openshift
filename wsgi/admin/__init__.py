from flask import Flask
from celery import Celery

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

app = Flask(__name__)
app.config.from_object('admin.conf')
wrk = make_celery(app)

# final reference
import admin.main
