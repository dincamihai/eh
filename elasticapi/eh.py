import requests

API = "https://api-lon-p.elastichosts.com"
USER = 'dincamihai'
SECRET_KEY = 'SECRET_KEY'

def servers_info():
    url = '/'.join([API, 'drives/list'])
    resp = requests.get(url, auth=(USER, SECRET_KEY))

if __name__ == '__main__':
    print servers_info()
