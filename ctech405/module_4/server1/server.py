import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_html():
    return ("<!DOCTYPE html><html><head><title>My first Flask web page</title></head><body><p>Hello world wide web!</p></body></html>")

app.run(host='0.0.0.0')
