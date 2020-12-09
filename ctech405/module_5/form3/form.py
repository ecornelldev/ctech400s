import flask
app = flask.Flask(__name__)

@app.route('/form')
def form_show():
    return flask.render_template('form.html')

@app.route('/done1')
def form_two_submit():
    return flask.render_template('result.html', fields = flask.request.args, url=flask.request.url, form = 'Form 1')

@app.route('/done2')
def form_one_submit():
    return flask.render_template('result.html', fields = flask.request.args, url=flask.request.url, form = 'Form 2')

app.run(host='0.0.0.0')
