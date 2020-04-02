#
# This file is USED by the wsgi engine

import sys
import os

# Defining local venv environment
HOME = os.path.dirname(os.path.realpath(__file__))
VENV = HOME + '/venv'
PYTHON_BIN = VENV + '/bin/python3'

# activate the venv
activate_this = "{}/bin/activate_this.py".format(VENV)
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# If not in python3, restart with python3
if sys.executable != PYTHON_BIN:
    os.execl(PYTHON_BIN, PYTHON_BIN, *sys.argv)

# Insert all path of the venv
sys.path.insert(0, '{v}/lib/python3.7/site-packages'.format(v=VENV))
sys.path.insert(0, '{v}/lib'.format(v=VENV))
sys.path.insert(0, '{v}'.format(v=HOME))

# Load the default app
from run import app

# Propagate the exceptions to get the right message in json
app.config.update(PROPAGATE_EXCEPTIONS=True)
