#!/bin/bash

apt-get install screen

screen
source ./venv/bin/activate
./venv/bin/python3 run.py
screen -d
