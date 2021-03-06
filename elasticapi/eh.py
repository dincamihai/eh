#!/usr/bin/env python

import os
import json
import requests
import flask

from collections import defaultdict

from flask import Flask, render_template, request

API = "https://api-lon-b.elastichosts.com"
USER = os.environ.get('USER_UUID', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

root = flask.Blueprint("index", __name__)

def drives_for_servers(servers_info, drives_info):
    output = defaultdict(list)
    drives_mapping = dict([[item['drive'], item['name']] for item in drives_info])
    for item in servers_info:
        drives = filter(lambda key: key.startswith('block'), item.keys())
        for key in drives:
            drive_uuid = item[key]
            output[item['name']].append(drives_mapping.get(drive_uuid))
    return output

def servers_info():
    drives_url = '/'.join([API, 'drives/info'])
    drives_resp = requests.get(
               drives_url,
               auth=(USER, SECRET_KEY),
               headers={'Accept': 'application/json'})

    servers_url = '/'.join([API, 'servers/info'])
    servers_resp = requests.get(
               servers_url,
               auth=(USER, SECRET_KEY),
               headers={'Accept': 'application/json'})

    if servers_resp.status_code == 200 and drives_resp.status_code == 200:
        return drives_for_servers(
                json.loads(servers_resp.text),
                json.loads(drives_resp.text))
    else:
        drives_resp.raise_for_status()
        servers_resp.raise_for_status()


@root.route("/")
def home():
    app = flask.current_app
    return render_template('layout.html', **{'info': servers_info()})

def initialize_app(app):
    app.register_blueprint(root)

if __name__ == '__main__':
    for name, drives in servers_info().items():
        print '%s: ' %name + ', '.join(drives)
