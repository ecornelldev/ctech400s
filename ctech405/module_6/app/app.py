import flask
app = flask.Flask(__name__)

@app.route('/')
def form_show():
    if 'message' not in flask.request.args:
        m = '(No message yet)'
    else:
        m = flask.request.args['message']
    return flask.render_template('form.html', msg = m)

app.run(host='0.0.0.0')
