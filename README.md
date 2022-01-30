Template for Redis using Python and Docker
==============================

What Is This?
-------------

This is a simple Python, Redis and Docker Template intended to provide a working module to write your own application using redis, python and docker.


How To Use This
---------------

1. Create a file `.env` and fill in the required ENV variables such as `IS_PRODUCTION` with data type of boolean and you can also add your database configurations here.
3. Create python virtual environment by typing `python3 -m venv {name of virtual environment}` and activate it by typing this command `. {name of virtual environment}/bin/activate`
2. Run `pip install -r requirements.txt` to install dependencies
6. Run `python main.py`


Production Deployment
----------------

For production deployment reasssign a new value for IS_PRODUCTION with a value of True to access your production configurations

