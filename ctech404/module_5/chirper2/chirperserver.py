import json, time, secrets
import flask
import basicdb

DATABASE = 'chirper.json'

# Setup
app = flask.Flask(__name__)
basicdb.load_db(DATABASE)

logins = {}
for row in basicdb.db_from('logins'):
    logins[row['userid']] = row['password']

sessions = {}

@app.route('/login', methods=['POST'])
def login():
    username = flask.request.headers['Username']
    password = flask.request.headers['Password']
    if username not in logins:
         return 'No such user', 401
    if password != logins[username]:
         return 'Invalid password', 401
    token = secrets.token_hex()
    sessions[token] = username
    return json.dumps({'token': token})
   
@app.route('/get-chirps')
def get_chirps():
    chirps = basicdb.orderby(basicdb.db_from('chirps'), 'time')[-5:]
    return json.dumps(chirps)

@app.route('/post-chirp', methods=['POST'])
def post_chirp():
    token = flask.request.headers['Token']
    if token not in sessions:
        return 'Invalid token', 401
    chirp = {'userid': sessions[token],
            'time': str(time.time()), 
            'text': flask.request.form['text']}
    if len(chirp['text']) > 100:
        return 'chirp too long', 403
    basicdb.insert('chirps', chirp)
    return 'chirp posted'



app.run(host='0.0.0.0')
