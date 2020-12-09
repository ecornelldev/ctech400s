import flask
app = flask.Flask(__name__)

@app.route('/form')
def form_show():
    return flask.render_template('form.html')

@app.route('/done')
def form_submit():
    m = flask.request.args['message']
    return flask.render_template('result.html', msg = m)

app.run(host='0.0.0.0')
