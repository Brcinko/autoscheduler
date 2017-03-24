# autoscheduler
This project is a part of master thesis named "Automation of virtual machine placement". This repository contains web interface for OpenStack scheduler automatization software - autoschEDUler.


## Prerequisities and installation guide

Here comes list of prerequisities, for now it is just:

* python 2.7.6
* pymongo
* pprint
* MongoDB
* json
* bson
* pprint
* requests

This section will be transformed into install guide later.

## Database scheme

autoschEDUler uses MongoDB which is noSQL database based on JSON (BSON) objects. 

Database for internal statistics and configurations has following structure:
  __collection_name__: configurations, __example_file__: [autoscheduler-web-interface/frontend/get_conf_example.json](https://github.com/Brcinko/autoscheduler-web-interface/blob/master/frontend/get_conf_example.json "autoschEDUler web interface")
  __collection_name__: hosts_statistics, __example_file__: [autoscheduler-web-interface/frontend/get_hosts_stats_example.json](https://github.com/Brcinko/autoscheduler-web-interface/blob/master/frontend/get_host_stats_example.json "autoschEDUler web interface")
  __collection_name__: hosts_list, __example_file__: [autoscheduler-web-interface/frontend/get_hosts_list_example.json](https://github.com/Brcinko/autoscheduler-web-interface/blob/master/frontend/get_hosts_list_example.json "autoschEDUler web interface")

## Authentication

Authentication with OpenStack (Ceilometer) is desirable. For that reason autoscheduler user
needs to be created in OpenStack module Keystone. Use these credential in stats_collector module to get auth token.



## TODO list

* updated later
