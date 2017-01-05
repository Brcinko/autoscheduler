# autoscheduler
This project is a part of master thesis named "Automation of virtual machine placement". This repository contains web interface for OpenStack scheduler automatization software - autoschEDUler.


##Prerequisities and installation guide

Here comes list of prerequisities, for now it is just:

* python 2.7.6
* pymongo
* pprint
* MongoDB
* json
* bson

This section will be transformed later into install guide.

##Database scheme

autoschEDUler recognize two separate databases which is working with. 
First database is internal autoschEDUler database for statistics and configuration save. This database is also common with autoschEDUler webinterface.
Second database is OpenStack Ceilometer database from which statistcs about physical machines are taken.

autoschEDUler uses MongoDB which is noSQL database based on JSON (BSON) objects. 

First mentioned database (only autoschEDUler) for internal statistics and configurations has following structure:
  __collection_name__: configurations, __example_file__: [autoscheduler-web-interface/frontend/get_conf_example.json](https://github.com/Brcinko/autoscheduler-web-interface/blob/master/frontend/get_conf_example.json "autoschEDUler web interface")

Second mentioned database (OpenStack Ceilometer) has following structure:
  _Not implemented yet_

##TODO list

* updated later
