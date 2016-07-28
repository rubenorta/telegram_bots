#!/usr/bin/env bash

ln -s /vagrant/dev/telegram_bots bot

# python
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install pydub
sudo apt-get install -y aubio-tools libaubio-dev libaubio-doc
sudo pip install telepot
sudo apt-get install -y libav-tools
sudo apt-get install -y git
sudo locale-gen UTF-8
sudo hostname snake