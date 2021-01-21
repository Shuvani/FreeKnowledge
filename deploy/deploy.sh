PROJECT_GIT_URL='https://github.com/Shuvani/knowfree.git'
PROJECT_BASE_PATH='/opt/venv'

sudo su -

echo "Installing dependencies..."
apt-get update
apt-get upgrade
apt-get install python3-dev python3-pip python3-venv nginx

# create virtual environment and activate it
python3 -m venv $PROJECT_BASE_PATH
source $PROJECT_BASE_PATH/bin/activate
pip install django gunicorn

# Create project directory
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH
cd $PROJECT_BASE_PATH

cp $PROJECT_BASE_PATH/Freeknowledge/freeknowledge/deploy/default /etc/nginx/sites-available/default

cd $PROJECT_BASE_PATH/FreeKnowledge
sudo apt-get install supervisor

cp $PROJECT_BASE_PATH/Freeknowledge/freeknowledge/deploy/gunicorn.conf.py $PROJECT_BASE_PATH/myproject/myproject/gunicorn.conf.py
cp $PROJECT_BASE_PATH/Freeknowledge/freeknowledge/deploy/myproject.conf /etc/supervisor/conf.d/myproject.conf

supervisorctl reread
supervisorctl update
supervisorctl status freeknowledge
supervisorctl restart freeknowledge

