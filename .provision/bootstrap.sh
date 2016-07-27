#!/usr/bin/env bash

ln -s /vagrant/dev/telegram_bots bot

# python
sudo apt-get install python-pip python-dev build-essential 
sudo pip install pydub
sudo apt-get install aubio-tools libaubio-dev libaubio-doc
sudo pip install telepot
sudo apt-get install libav-tools
