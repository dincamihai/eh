ElasticAPI
==========

Instructions
------------

1. Clone the repository::

    $ git clone https://github.com/dincamihai/eh.git
    $ cd eh

2. Create a virtualenv and install dependencies::

    $ virtualenv sandbox
    $ echo '*' > sandbox/.gitignore
    $ . sandbox/bin/activate
    $ pip install -r requirements-dev.txt

3. Set user UUID and SECRET_KEY in environment::

    $ export USER_UUID=<your user UUID>
    $ export SECRET_KEY=<your secret key>

4. Run the application

    as a server::

    $ cd elasticapi
    $ gunicorn manage:app

    and view the output in browser: http://localhost:8000

    OR

    in terminal::

    $ ./eh.py
