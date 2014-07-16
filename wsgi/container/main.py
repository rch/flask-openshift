import os, flask, utils
from flask import Response, url_for, render_template, current_app, make_response
from datetime import datetime, timedelta
from container import app


app.config.update(dict(
    ADMINDB=os.path.join(app.root_path, 'admin.db'),
    DEBUG=True,
    SECRET_KEY='public string',
    ADMINUSER='admin',
    ADMINPASS='default'
))
app.config.from_envvar('FLASK_MAIN', silent=True)


@app.route('/')
def show_entries():
    db = utils.get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('base-view.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not flask.session.get('logged_in'):
        abort(401)
    db = utils.get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [flask.request.form['title'], flask.request.form['text']])
    db.commit()
    flask.flash('New entry was successfully posted')
    return flask.redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if flask.request.method == 'POST':
        if flask.request.form['username'] != app.config['ADMINUSER']:
            error = 'Invalid username'
        elif flask.request.form['password'] != app.config['ADMINPASS']:
            error = 'Invalid password'
        else:
            flask.session['logged_in'] = True
            flask.flash('You were logged in')
            return flask.redirect(url_for('show_entries'))
    return render_template('base-login.html', error=error)


@app.route('/logout')
def logout():
    flask.session.pop('logged_in', None)
    flask.flash('You were logged out')
    return flask.redirect(url_for('show_entries'))


@app.route('/initdb')
def init_db():
    """Creates the database tables."""
    utils.init_db()
    return 'Initialized the database.'


# @app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    utils.init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    current_db = utils.get_db()
    if current_db is not None:
        current_db.close()
