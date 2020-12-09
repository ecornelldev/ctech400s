import requests, sys
from spotifysecrets import *
from base64 import b64encode
import requestview

AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'

# Authenticate with Spotify
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)

token = r.json()['access_token']
token_headers = {'Authorization' : 'Bearer ' + token}

SEARCH_URL = 'https://api.spotify.com/v1/search'

# Find top artist matching the user's search
artist_name = ' '.join(sys.argv[1:])
query = {'q': artist_name, 'type': 'artist'}
r = requests.get(SEARCH_URL, headers=token_headers, params=query)

requestview.view(r)
