#!/bin/bash

sudo su -

echo "Updating project..."

PROJECT_BASE_PATH='/data/venv/freeknowledge'

source /data/venv/bin/activate

cd $PROJECT_BASE_PATH
git pull
python3 $PROJECT_BASE_PATH/freeknowledge/manage.py migrate
python3 $PROJECT_BASE_PATH/freeknowledge/manage.py collectstatic --noinput
supervisorctl restart freeknowledge

echo "DONE! :)"
