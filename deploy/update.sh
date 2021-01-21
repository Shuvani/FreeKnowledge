#!/usr/bin/venv bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/FreeKnowledge'

git pull
$PROJECT_BASE_PATH/venv/bin/python $PROJECT_BASE_PATH/freeknowledge/manage.py migrate
$PROJECT_BASE_PATH/venv/bin/python $PROJECT_BASE_PATH/freeknowledge/manage.py collectstatic --noinput
supervisorctl restart freeknowledge

echo "DONE! :)"
