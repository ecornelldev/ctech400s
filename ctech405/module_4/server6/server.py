import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template('count.html', integers=range(0,1000,2))

app.run(host='0.0.0.0')
