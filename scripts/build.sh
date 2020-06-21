#!/bin/bash
set -e

mysql -uroot -e "CREATE USER 'dev_user'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'dev_user'@'localhost';"
python3 remotehat/manage.py test hat
