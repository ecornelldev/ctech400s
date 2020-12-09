import flask
app = flask.Flask(__name__)

@app.route('/<x>')
def hello(x):
    return 'You requested the page "' + x + '".'

app.run(host='0.0.0.0')