import flask

app = flask.Flask(__name__)

f = open("pride.txt")

@app.route('/')
def pride_main():
    return flask.render_template('pride.html')

@app.route('/pride')
def pride_paragraph():
    return f.readline()
    
app.run(host='0.0.0.0')

