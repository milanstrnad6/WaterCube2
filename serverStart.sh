#!/bin/bash

sudo fuser 80/tcp -k
export FLASK_APP=/home/pi/CUBE/API.py
sudo -E flask run --host=0.0.0.0 --port=80
