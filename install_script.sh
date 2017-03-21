
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
echo "5 0 * 1-5 autoscheduler python /home/brcinko/db/autoscheduler/main.py" >> mycron
#install new cron file
crontab mycron

