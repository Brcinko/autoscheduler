"""
    stats_collector, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

import db_connector
import settings
import requests
import pprint
import helpers
import json
import datetime


def ceilometer_auth():
    r = requests.post(settings.KEYSTONE_ADDRESS)
    pprint.pprint(r.text)
    uri = settings.KEYSTONE_ADDRESS + settings.KEYSTONE_TOKEN_ROUTE
    r = requests.post(uri, data='{"auth": {"tenant": "netcell-testing", "passwordCredentials": {"username":"admin", "password":"TATKO"}}}')
    pprint.pprint(r.text)
    response = r.json()
    print response['access']['token']['id']
    return response['access']['token']['id']


# Get stats from Ceilometer
# Match stats for meters and ISODate
def get_stats(token):
    header = {"X-Auth-Token": token}
    uri = settings.CEILOEMETER_ADDRESS + settings.CEILOMETER_SAMPLE_ROUTE
    r = requests.get(uri, headers=header)
    # print r.json()
    stats = r.json()
    pprint.pprint(stats)
    for s in stats:
        # if s['timestamp']
        sample_date = datetime.strptime(s['timestamp'], "%Y-%m-%d %H:%M:%S")
        if sample_date == datetime.date.today():
            print str(sample_date)
        else:
            print str(datetime.date.today())
    return stats


# Serialize pairs of stats from Ceilometer
# Put serialized stats into autoscheduler_db
def save_stats(stats):
    db = db_connector.connect_to_db()
    collection = db_connector.get_collection(collection_name='hosts_statistics', db=db)
    serialized_stats = {}
    for s in stats:
        db_connector.add_document(collection=collection, query=s)


token = helpers.openstack_auth()
get_stats(token=token)
# save_stats()
