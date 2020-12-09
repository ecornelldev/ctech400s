import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    words = ['swordfish', 'xyzzy', 'Tyler sent me']
    return flask.render_template('secret.html', secretwords=words)

app.run(host='0.0.0.0')
