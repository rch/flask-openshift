import os
DEBUG = True
SECRET_KEY = 'FIXME_SECRET'
try:
    FREEZER_DESTINATION = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'frozen')
except AttributeError:
    pass

# postgresql
PG_HOST = os.getenv('OPENSHIFT_POSTGRESQL_DB_HOST', 'localhost')
PG_PORT = os.getenv('OPENSHIFT_POSTGRESQL_DB_PORT', 5432)
PG_USER = os.getenv('OPENSHIFT_POSTGRESQL_DB_USERNAME', os.getenv('PG_USER'))
PG_PASS = os.getenv('OPENSHIFT_POSTGRESQL_DB_PASSWORD', os.getenv('PG_PASS'))
PG_NAME = os.getenv('OPENSHIFT_APP_NAME', os.getenv('PG_NAME'))

try:
    assert None not in [PG_NAME, PG_PASS, PG_USER, PG_PORT, PG_HOST]
except AssertionError as e:
    print 'edit admin/conf.py or configure environment:'
    print 'export PG_USER=_username_'
    print 'export PG_PASS=_password_'
    print 'export PG_NAME=_database_'
    raise e

POSTGRES = {
    'host': PG_HOST,
    'port': PG_PORT,
    'u': PG_USER,
    'pw': PG_PASS,
    'db': PG_NAME,
}
BROKER_URL = 'sqla+postgresql://{u}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)
CELERY_RESULT_ENGINE_OPTIONS = {'echo': False}
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_BACKEND = 'db+postgresql://{u}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)
CELERY_RESULT_DB_TABLENAMES = {
    'task': 'flask_taskmeta',
    'group': 'flask_groupmeta',
}
