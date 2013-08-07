import requests
import os
import json

from collections import defaultdict

API = "https://api-lon-b.elastichosts.com"
USER = os.environ.get('USER_UUID', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

def drive_name(drive_uuid):
    url = '/'.join([API, 'drives/{DRIVE}/info'.format(DRIVE=drive_uuid)])
    resp = requests.get(
               url,
               auth=(USER, SECRET_KEY),
               headers={'Accept': 'application/json'})
    if resp.status_code == 200:
        return json.loads(resp.text)['name']
    else:
        return ''

def drives_for_servers(servers_info):
    output = defaultdict(list)
    for item in servers_info:
        drives = filter(lambda key: key.startswith('block'), item.keys())
        for key in drives:
            drive_uuid = item[key]
            output[item['name']].append(drive_uuid)
    return output

def servers_info():
    url = '/'.join([API, 'servers/info'])
    resp = requests.get(
               url,
               auth=(USER, SECRET_KEY),
               headers={'Accept': 'application/json'})
    if resp.status_code == 200:
        return drives_for_servers(json.loads(resp.text))
    else:
        resp.raise_for_status()

if __name__ == '__main__':
    print servers_info()
