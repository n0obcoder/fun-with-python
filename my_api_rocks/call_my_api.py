import sys

def q(text=''):
    print(f'>{text}<')
    sys.exit() 

from pprint import pprint
import requests

url_1 = 'http://127.0.0.1:5000/that_boi?name=deepi'
url_2 = 'http://127.0.0.1:5000/that_boi'
url_3 = 'http://127.0.0.1:5000/that_boi?name=deep'
url_4 = 'http://127.0.0.1:5000/that_boi?naaaam=deepi'
url_5 = 'http://127.0.0.1:5000/that_boi?name=sammy boy'

url = url_5
print('url called: {}\n'.format(url))

response = requests.get(url)
# pprint(response.json())
# print('response.content    : ', response.content)
# print('response.status_code: ', response.status_code)

try: # try is used here because there can be bad responses which needs to be taken care of. I am not going to go into much depth for now.
    print('${}$ got skill a-\n{} '.format(response.json()['name'], response.json()['skill']))
except:
    print('wrong input')



''' 
RESPONSE STATUS CODES: https://www.dataquest.io/blog/python-api-tutorial/

Informational responses (100–199),
Successful responses (200–299),
Redirects (300–399),
Client errors (400–499),
and Server errors (500–599).
'''
