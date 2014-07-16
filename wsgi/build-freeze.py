from flask_frozen import Freezer
from container import app


build = Freezer(app)

if __name__ == '__main__':
    print 'destination:', build.root
    build.freeze()
