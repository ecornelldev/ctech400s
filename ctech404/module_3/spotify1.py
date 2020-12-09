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

requestview.view(r)
