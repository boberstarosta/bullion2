#!/bin/bash

sudo apt-get -y install screen </dev/null

screen
source ./venv/bin/activate
./venv/bin/python3 manage.py runserver localhost:8080 --noreload
screen -d
