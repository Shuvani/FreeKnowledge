#!/usr/bin/venv bash

#set -e
sudo su -

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/Shuvani/knowfree.git'

PROJECT_BASE_PATH='/usr/local/apps/FreeKnowledge'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python3-pip supervisor nginx git

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/venv
python3 -m venv $PROJECT_BASE_PATH/venv
#source $PROJECT_BASE_PATH/venv/bin/activate # под вопросом

# Install python packages
$PROJECT_BASE_PATH/venv/bin/pip install wheel
$PROJECT_BASE_PATH/venv/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/venv/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/venv/bin/python3 $PROJECT_BASE_PATH/freeknowledge/manage.py migrate
$PROJECT_BASE_PATH/venv/bin/python3 $PROJECT_BASE_PATH/freeknowledge/manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/freeknowledge/deploy/freeknowledge.conf /etc/supervisor/conf.d/freeknowledge.conf
supervisorctl reread
supervisorctl update
supervisorctl restart freeknowledge

# Configure nginx
cp $PROJECT_BASE_PATH/freeknowledge/deploy/nginx_freeknowledge.conf /etc/nginx/sites-available/freeknowledge.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/freeknowledge.conf /etc/nginx/sites-enabled/freeknowledge.conf
systemctl restart nginx.service

echo "DONE! :)"







# проверенное
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-dev python3-pip python3-venv nginx

sudo su -
sudo python3 -m venv /opt/venv
source /opt/venv/bin/activate
pip install django gunicorn

cd /opt/venv
django-admin.py startproject myproject
cd myproject
vim settings.py #add public ip to allowed hosts
cd ../
gunicorn myproject.wsgi:application --bind 172.31.43.21:8000 #private ip

cd /etc/nginx/sites-available/
sudo vim default
# delete everything from file and write there
server {
    listen 80;
    server_name 3.10.215.109; #либо public ip, либо доменное имя
    access_log  /var/log/nginx/example.log;

    location /static/ {
        root /opt/venv/myproject/;
        expires 30d;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
#

cd /opt/venv/myproject
sudo service nginx restart
gunicorn myproject.wsgi:application #it works

sudo apt-get install supervisor
cd /opt/venv/myproject/myproject
touch gunicorn.conf.py
sudo vim gunicorn.conf.py
# write there
  bind = '127.0.0.1:8000'
  workers = 3
  user = "nobody"
#

cd /etc/supervisor/conf.d/
sudo touch myproject.conf
sudo vim myproject.conf
# write there
  [program:myproject]
  command=/opt/venv/bin/gunicorn myproject.wsgi:application -c /opt/venv/myproject/myproject/gunicorn.conf.py
  directory=/opt/venv/myproject
  user=nobody
  stdout_logfile=/home/myproject.log
  stderr_logfile=/home/myproject.log
  autostart=true
  autorestart=true
  redirect_stderr=true
#

supervisorctl reread
supervisorctl update
supervisorctl status myproject
supervisorctl restart myproject