import requests
import sys

WP_URL = 'https://en.wikipedia.org/wiki/'
page = sys.argv[1]

r = requests.get(WP_URL + page)
print(r.text)
