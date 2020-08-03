import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template('hello.html')

app.run(host='0.0.0.0')