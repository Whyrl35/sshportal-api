# INSTALLATION

# API of sshportal

## How to quick install

```commandline
# cd /__your_path__/
# git clone __this_repository__
# cd __repository__
# virtualenv -p python3 venv
# source venv/bin/activate
# pip install -r requirements.txt
```

## Migrate your database to be compatible

```commandline
# export FLASK_APP=run.py
# flask db upgrade
```

## How to test installation

```commandline
# export FLASK_APP=run.py
# flask run
```

## Docker

### Pull the image

```
docker pull whyrl/sshportal-api:latest
```

### configuration

Put a configuration file in /srv/sshportal-api/  (see the repository for a conf.yml.sample)
Edit it and set the needed information to access sqlite or mysql
For sqlite set the absolute path to your sshportal.db

### Run a container

```
docker run -d --rm -n sshportal-api -v /srv/sshportal-api:/data -p 8000:8000 whyrl/sshportal-api:latest
```

### Upgrade database the first time

When installing the API for the first time, upgrade the database to add necessary table/column

```
docker exec -it sshportal-api FLAKS_APP=run.py flask db upgrade
docker restart sshportal-api
```

### Next

You can add a Nginx in front of the container.
Gunicorn run inside the container (with default value, may be updated for better performance)

## What to do next ?

You need a WSGI server in front of the flask APP.\
You can either :

* Install Apache2 + mode UWSGI
* Install nginx + gunicorn

