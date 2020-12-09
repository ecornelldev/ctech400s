import flask
app = flask.Flask(__name__)

story = []

@app.route('/')
def story_start():
    global story
    story = []
    return flask.render_template('start.html')

@app.route('/add', methods=['POST'])
def story_continue():
    global story
    m = flask.request.form['new-text']
    story.append(m)
    return flask.render_template('add.html', words = story)

app.run(host='0.0.0.0')
