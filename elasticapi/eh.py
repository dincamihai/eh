import requests
import os

API = "https://api-lon-b.elastichosts.com"
USER = os.environ.get('USER_UUID', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

def servers_info():
    url = '/'.join([API, 'drives/list'])
    resp = requests.get(
               url,
               auth=(USER, SECRET_KEY),
               headers={'Accept': 'application/json'})
    return resp.text

if __name__ == '__main__':
    print servers_info()
