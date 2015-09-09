FROM ubuntu:14.04

COPY requirements.txt /forumkyiv.org/requirements.txt

RUN apt-get update && apt-get install -y python-dev python-pip g++ libjpeg62-dev zlib1g-dev && \
    cd /forumkyiv.org && pip install -r requirements.txt

COPY manage.py /forumkyiv.org/manage.py
COPY forumkyiv/ /forumkyiv.org/forumkyiv
COPY locale/ /forumkyiv.org/locale
COPY static/ /forumkyiv.org/static
COPY core/ /forumkyiv.org/core
COPY db.sqlite3 /forumkyiv.org/db.sqlite3
COPY media/ /forumkyiv.org/media
COPY copy_db_and_media_to_static.sh /forumkyiv.org/copy_db_and_media_to_static.sh


WORKDIR /forumkyiv.org
RUN chmod a+x /forumkyiv.org/manage.py && \
    python /forumkyiv.org/manage.py migrate --noinput && python /forumkyiv.org/manage.py update_index && \
    python manage.py collectstatic --noinput

CMD python /forumkyiv.org/manage.py runserver 0.0.0.0:8000
EXPOSE 8000