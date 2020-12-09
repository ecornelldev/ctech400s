import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template('template.html', secretword = flask.request.args['password'])

app.run(host='0.0.0.0')
