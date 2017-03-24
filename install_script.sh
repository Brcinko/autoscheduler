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

# create cron for stats_collector
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 0 * 1-5 python /home/brcinko/db/autoscheduler/main.py" >> mycron
#install new cron file
crontab mycron