import flask
app = flask.Flask(__name__)

@app.route('/form')
def form_show():
    return flask.render_template('form.html')

@app.route('/done', methods=['POST'])
def form_submit():
    m = flask.request.form['message']
    return flask.render_template('result.html', msg = m)

app.run(host='0.0.0.0')
