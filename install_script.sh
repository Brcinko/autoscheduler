#!/bin/bash

# ak chcem pridat pre suda tak dam iba ze sudo crontab -e a hotovo
# autoscheduler heslo je heslo
# create autoscheduler user - add to openstack group for nova.conf modification
# -----CHANGE GROUP NAME--------
sudo groupadd openstack
sudo useradd -G openstack autoscheduler
id autoscheduler 

# create cron for autoscheduler - main.py
# ----CHANGE DIRECTORY------
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "30 0 * 1-5 autoscheduler python /home/brcinko/db/autoscheduler/main.py" >> mycron
#install new cron file
crontab mycron


sudo apt-get install python, python-pip, mongo, git

git clone --recursive https://github.com/Brcinko/autoscheduler.git
cd austoscheduler/

# execute next sentence of commands into mongo shell
# >use autoscheduler_db
# >db.hosts_list.add()
# >db.configurations.add()
# >db.hosts_statistics.add()
# >exit

useradd autoscheduler
passwd autoscheduler


sudo pip install –r requirements.txt

