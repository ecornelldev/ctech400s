from flask import *
from basicdb import *

app = Flask(__name__)
load_db('geo.json')

@app.route('/lookup/<zipcode>')
def lookup(zipcode):
    rows = where(db_from('geozipcodes'), 'Zip Code', zipcode)
    text = zipcode + ' is in ' + rows[0]['City'] + ', ' + rows[0]['State']
    return text

app.run(host='0.0.0.0', port=3000)