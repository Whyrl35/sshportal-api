#!/usr/bin/env python

import os
import sys
from getpass import getpass


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

import argparse

BASE_DIR = HOME
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

from resources.models import UserModel


def register(user, password):
    userobj = UserModel.find_by_username(user)

    if not userobj:
        return 'User {} do not exists, create it via sshportal command line'.format(user)

    password = getpass('Please enter your password: ')

    userobj.password = UserModel.generate_hash(password)
    userobj.is_admin = True

    try:
        userobj.save_to_db()
        return 'User {} updated'.format(user)
    except:
        return 'Something went wrong'


def exists(user):
    if UserModel.find_by_username(user):
        print('User {} already exists'.format(user))
        sys.exit(0)
    else:
        print("User don't exsist")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description='Add a new user into the database',
            epilog='For any question on this script, please contact ludovic.houdayer@corp.ovh.com'
            )

    parser.add_argument('--exist', help='launch a test on user', action='store_true', default=False)
    parser.add_argument('--user', help='A user name', metavar='john', type=str, required=True)
    parser.add_argument('--password', help='A password', metavar='my_secrets', type=str, required=False)
    args = parser.parse_args()

    if args.exist:
        exists(args.user)
    elif not args.password:
        print(register(args.user, None))
    else:
        print(register(args.user, args.password))
