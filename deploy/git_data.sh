#!/usr/bin/expect -f

PROJECT_GIT_URL='https://github.com/Shuvani/FreeKnowledge.git'
PROJECT_BASE_PATH='/data/venv/freeknowledge'

spawn git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH
expect "Username for 'https://github.com': "
send "Shuvani\r"
expect "Password for 'https://Shuvani@github.com': "
interact ++ return
send "\r"
expect eof