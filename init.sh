#!/bin/sh
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/django.py /etc/gunicorn.d/django.py
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start