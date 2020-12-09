import flask
app = flask.Flask(__name__)

users = {'ac203': 'Alice Chin',
         'bm227': 'Betrand Marks',
         'cp440':  'Cassandra Poe'}

@app.route('/<username>')
def user_homepage(username):
    if username in users:
        return 'This is the homepage for ' + users[username] + '.'
    else:
        return 'No such user.', 404

app.run(host='0.0.0.0')