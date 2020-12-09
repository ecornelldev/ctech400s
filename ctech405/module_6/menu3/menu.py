import flask
from basicdb import *

app = flask.Flask(__name__)

load_db('menu.json')

def get_sections():
    return distinct(select(orderby(db_from('items'), 'Section'), 'Section'))

@app.route('/')
@app.route('/menu')
def menu():
    items_list = db_from('items')
    return flask.render_template('menu.html', items = items_list, sections =  get_sections())

@app.route('/submenu')
def submenu():
    section = flask.request.args['section']
    items_list = where(db_from('items'), 'Section', section)
    return flask.render_template('submenu.html',
                           section = section,
                           items = items_list,
                           sections =  get_sections())

@app.route('/add', methods=['POST'])
def add():
    new_item = {'Name': flask.request.form['name'],
               'Price': flask.request.form['price'],
               'Section': flask.request.form['section']}
    insert('items', new_item)
    return flask.render_template('add.html',
                           added_item = new_item,
                           sections = get_sections())

app.run(host='0.0.0.0')
