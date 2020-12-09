import flask
app = flask.Flask(__name__)

counter = 0

@app.route('/')
def keep_count():
    global counter
    counter = counter + 1
    return 'The counter is now ' + str(counter)

app.run(host='0.0.0.0')