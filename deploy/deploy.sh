#!/bin/bash

sudo su -

PROJECT_GIT_URL='https://github.com/Shuvani/FreeKnowledge.git'

PROJECT_BASE_PATH='/data/venv/freeknowledge'

echo "Installing dependencies..."
apt-get update
yes | apt-get upgrade
yes | apt-get install python3-dev python3-pip python3-venv nginx git nodejs npm supervisor expect

# create virtual environment and activate it
python3 -m venv /data/venv
source /data/venv/bin/activate

#install gunicorn
pip install gunicorn

# Create project directory
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

#install project dependencies
pip install -r $PROJECT_BASE_PATH/requirements.txt
cd $PROJECT_BASE_PATH/freeknowledge/static/js
npm install

#configure nginx
cp $PROJECT_BASE_PATH/deploy/default /etc/nginx/sites-available/default
cd $PROJECT_BASE_PATH
python3 manage.py migrate
python3 manage.py collectstatic
service nginx restart

# configure supervisor
#apt-get install supervisor
cp $PROJECT_BASE_PATH/deploy/gunicorn.conf.py $PROJECT_BASE_PATH/freeknowledge/
cp $PROJECT_BASE_PATH/deploy/freeknowledge.conf /etc/supervisor/conf.d/

supervisorctl reread
supervisorctl update
supervisorctl status freeknowledge
supervisorctl restart freeknowledge

echo "DONE! :)"

