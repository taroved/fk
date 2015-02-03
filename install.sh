#!/bin/sh

apt-get update && apt-get install -y python-dev python-pip g++ libjpeg62-dev zlib1g-dev

cd /forumkyiv.org && pip install -r requirements.txt

chmod a+x /forumkyiv.org/install.sh
chmod a+x /forumkyiv.org/manage.py

python /forumkyiv.org/manage.py migrate --noinput && python /forumkyiv.org/manage.py update_index