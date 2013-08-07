#!/usr/bin/env python

import eh

import flask
import flaskext.script

def create_app(instance_path=None):
    app = flask.Flask(__name__.split('.')[0],
                      instance_path=instance_path,
                      instance_relative_config=True)
    eh.initialize_app(app)
    return app

app = create_app()

manager = flaskext.script.Manager(app)

if __name__ == '__main__':
    manager.run()
