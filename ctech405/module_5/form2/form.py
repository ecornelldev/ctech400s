import flask
app = flask.Flask(__name__)

@app.route('/form')
def form_show():
    return flask.render_template('form.html')

@app.route('/done')
def formSubmit():
    return flask.render_template('result.html', fields = flask.request.args, url = flask.request.url)

app.run(host='0.0.0.0')
