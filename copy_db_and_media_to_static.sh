#!/bin/sh
rm  ./static/media.tar.gz -f
rm  ./static/db.sqlite3 -f
cp db.sqlite3 ./static/
tar -zcvf ./static/media.tar.gz ./media
echo 'Done'