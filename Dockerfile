FROM ubuntu:14.04

COPY core/ /forumkyiv.org/core
COPY forumkyiv/ /forumkyiv.org/forumkyiv
COPY locale/ /forumkyiv.org/locale
COPY static/ /forumkyiv.org/static
COPY media/ /forumkyiv.org/media
COPY manage.py /forumkyiv.org/manage.py
COPY requirements.txt /forumkyiv.org/requirements.txt
COPY db.sqlite3 /forumkyiv.org/db.sqlite3
COPY install.sh /forumkyiv.org/install.sh
COPY copy_db_and_media_to_static.sh /forumkyiv.org/copy_db_and_media_to_static.sh


WORKDIR /forumkyiv.org
RUN ./install.sh

CMD python /forumkyiv.org/manage.py runserver 0.0.0.0:8000
EXPOSE 8000