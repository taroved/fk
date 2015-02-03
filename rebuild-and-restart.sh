#!/bin/sh

cd /root/forumkyiv.org
docker build --force-rm --rm -t forumkyiv .
docker stop forumkyiv.org
docker rm forumkyiv.org
docker run -d --name forumkyiv.org -p 8001:8000 gahsc
cd /root
./restart-nginx.sh