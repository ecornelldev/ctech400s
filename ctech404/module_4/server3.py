import random
import flask
app = flask.Flask(__name__)

@app.route('/')
def die_roll():
    return 'You rolled a ' + str(random.randint(1,6))

app.run(host='0.0.0.0')