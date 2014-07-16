from flask import Flask 
from local.genshi import Genshi
import utils

app = Flask(__name__)

app.config.from_object('container.conf')

genshi = Genshi(app)

wrk = utils.make_celery(app)

utils.register_blueprints(app)

# final reference
import container.main
