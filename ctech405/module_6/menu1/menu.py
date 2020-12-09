import flask
from basicdb import *

app = flask.Flask(__name__)

load_db('menu.json')

@app.route('/')
def menu():
    items_list = db_from('items')
    return flask.render_template('menu.html', items = items_list)

app.run(host='0.0.0.0')
