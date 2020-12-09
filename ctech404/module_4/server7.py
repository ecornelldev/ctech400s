from flask import *
app = Flask(__name__)

@app.route('/decoder')
def decoder():
    s = 'Welcome to the secret message decoder.'
    if 'message' in request.args:
        s += '  The message is  ' + request.args['message'] + '.'
    else:
        s += '  Error: no message!'
        
    if 'secret' in request.args:
        s += '  You found the easter egg!'

    return s

app.run(host='0.0.0.0')