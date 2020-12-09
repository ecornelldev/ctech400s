import requests
import sys

URL = "https://en.wikipedia.org/w/api.php"
query = sys.argv[1]
PARAMS = {
    'action': 'query',
    'list': 'search',
    'srsearch': query,
    'format': 'json'
}

r = requests.get(url=URL, params=PARAMS)
data = r.json()

print('Top five results for ' + query + ' on Wikipedia')
print('----------------')

for result in data['query']['search'][:5]:
    print (result['title'])
