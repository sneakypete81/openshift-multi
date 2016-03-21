#!/usr/bin/python
import os

virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

# Route to the correct app based on subdomain
# Adapted from http://flask.pocoo.org/docs/0.10/patterns/appdispatch/
from werkzeug.exceptions import NotFound
from subdomain_dispatcher import SubdomainDispatcher
from apps.test1.test1 import app as test1_app
from apps.test2.test2 import app as test2_app
from apps.camlib.camlib import app as camlib_app

SUBDOMAIN_MAP = {
    "test1": test1_app,
    "test2": test2_app,
    "camblib": camlib_app,
}

def make_app(subdomain):
    if subdomain in SUBDOMAIN_MAP:
        return SUBDOMAIN_MAP[subdomain]
    else:
        return NotFound

application = SubdomainDispatcher('peteburgers.tk', make_app)

# No testing at this level - test from within the individual apps instead
