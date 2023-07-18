#!/bin/bash

#clone repo
#git clone https://github.com/Rulios/so-semestral-speedrun.git

#cd so-semestral-speedrun/vm/mgomx-reverse-proxy/

#chmod +x init-reverse-proxy.sh

#./init-reverse-proxy.sh

# Update package list and install Python 3 and Pip
sudo apt update
sudo apt install nginx

sudo ufw allow 'Nginx HTTP'

sudo cp ./nginx.conf /etc/nginx/nginx.conf

sudo systemctl restart nginx

#systemctl status nginx