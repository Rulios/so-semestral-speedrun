#!/bin/bash

#clone repo
#git clone https://github.com/Rulios/so-semestral-speedrun.git

#cd so-semestral-speedrun/vm/webserver/

#chmod +x init-server.sh

#./init-server.sh

# Update package list and install Python 3 and Pip
sudo apt update
sudo apt install python3 python3-pip

# Install packages from requirements.txt
pip3 install -r requirements.txt

python3 main.py