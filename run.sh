#!/bin/bash

if [ "$1" != "" ]; then
	python manage.py $@
	exit
else

    cp nginx.conf /etc/nginx/sites-available/
    LINK_FILE='/etc/nginx/sites-enabled/module'

    if [ -f $LINK_FILE ]; then
        rm $LINK_FILE
    fi

    ln -s /etc/nginx/sites-available/nginx.conf $LINK_FILE
    service nginx restart

    service redis-server start
    nohup celery -A stream worker -l info > worker &
    nohup celery -A stream beat -l info > beat &
    /usr/bin/uwsgi --ini stream.ini --uid root --gid www-data
fi
