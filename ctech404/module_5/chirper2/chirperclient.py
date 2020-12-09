import requests, sys

BASE_URL= 'http://localhost'
PORT = ":5000"

GET_ENDPOINT = BASE_URL + PORT + '/get-chirps'
POST_ENDPOINT = BASE_URL + PORT + '/post-chirp'
LOGIN_ENDPOINT = BASE_URL + PORT + '/login'

def login():
    u = input('Enter username: ')
    p = input('Enter password: ')
    r = requests.post(LOGIN_ENDPOINT, headers={'Username': u, 'Password': p})
    if r.ok:
        print(u + ' logged in')
        return r.json()['token']
    else:
        print(r.text)
        sys.exit()

 
def get_chirps():
    r = requests.get(GET_ENDPOINT)
    if r.ok:
        print('-----chirps-----')
        for chirp in reversed(r.json()):
            print(chirp['userid'] + ' -> ' + chirp['text'])
        print('---------------')
    else:
        print('Error: ' + r.text)

 
def post_chirp(token):
    t = input('Enter your chirp: ')
    r = requests.post(POST_ENDPOINT, data={'text': t}, headers={'Token':token})
    if r.ok:
        print('chirp posted')
    else:
        print('Error: ' + r.text)




print('Welcome to chirper!')
token = login()
while True:
    print('(0) quit')
    print('(1) read chirps')
    print('(2) post chirp')
    i = input('Enter command : ')
    if i == '0':
        break
    elif i == '1':
        get_chirps()
    elif i == '2':
        post_chirp(token)        
    else:
        print('Illegal command. Please try again.')
