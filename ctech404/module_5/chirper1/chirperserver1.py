import json, time
import flask
import basicdb

DATABASE = 'chirper.json'

# Setup
app = flask.Flask(__name__)
basicdb.load_db(DATABASE)
   
@app.route('/get-chirps')
def get_chirps():
    chirps = basicdb.orderby(basicdb.db_from('chirps'), 'time')[-5:]
    return json.dumps(chirps)

@app.route('/post-chirp', methods=['POST'])
def post_chirp():
    chirp = {'userid': flask.request.form['user'],
            'time': str(time.time()), 
            'text': flask.request.form['text']}
    if len(chirp['text']) > 100:
        return 'chirp too long', 403
    basicdb.insert('chirps', chirp)
    return 'chirp posted'



app.run(host='0.0.0.0')
