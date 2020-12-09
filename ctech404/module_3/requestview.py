import sys
import requests
from requests_toolbelt.utils import dump

def view(r):
    data = dump.dump_all(r, request_prefix = '', response_prefix='')
    print('\n' + data.decode('utf-8') + '\n\n')
