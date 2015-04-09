#!/bin/bash

echo "Attempting to kill uwsgi..."
killall uwsgi
sleep 1

echo "Starting a new uwsgi instance..."
uwsgi --socket :8000 --wsgi-file wsgi.py &> /dev/null &

