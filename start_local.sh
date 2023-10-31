#!/usr/bin/env bash

# install deps
python3 -m pip3 install --no-cache-dir -q -r requirements.txt
sudo apt-get --allow-releaseinfo-change update -qq && apt install -qq libgl1-mesa-glx libglib2.0-0 -y

# start local
python3 ocr_server.py >/dev/null 2>&1