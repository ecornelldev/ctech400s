import requests, sys

BASE_URL= 'http://localhost'
PORT = ":5000"

GET_ENDPOINT = BASE_URL + PORT + '/get-chirps'
POST_ENDPOINT = BASE_URL + PORT + '/post-chirp'


def login():
    u = input('Enter username: ')
    return u
 
def get_chirps():
    r = requests.get(GET_ENDPOINT)
    if r.ok:
        print('-----chirpS-----')
        for chirp in reversed(r.json()):
            print(chirp['userid'] + ' -> ' + chirp['text'])
        print('---------------')
    else:
        print('Error: ' + r.text)

 
def post_chirp(userid):
    t = input('Enter your chirp: ')
    r = requests.post(POST_ENDPOINT, data={'text': t, 'user' : userid})
    if r.ok:
        print('chirp posted')
    else:
        print('Error: ' + r.text)




print('Welcome to chirper!')
u = login()
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
        post_chirp(u)        
    else:
        print('Illegal command. Please try again.')
