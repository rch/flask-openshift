from flask_frozen import Freezer
from admin import app


build = Freezer(app)

if __name__ == '__main__':
    print 'destination:', build.root
    build.freeze()
