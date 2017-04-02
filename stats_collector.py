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
from datetime import datetime
from datetime import date


# Get stats from Ceilometer
# Match stats for meters and ISODate
def get_stats(token):
    header = {"X-Auth-Token": token}
    uri = settings.CEILOEMETER_ADDRESS + settings.CEILOMETER_SAMPLE_ROUTE
    r = requests.get(uri, headers=header)
    samples = r.json()
    # pprint.pprint(samples)

    stats = {}
    stats['sample_stat'] = []
    for s in samples:
        # TODO switch commented condition !!!! IMPORTANT !!!!
        sample_date = datetime.strptime(s['timestamp'][:10], "%Y-%m-%d")
        if sample_date == datetime.strptime("2017-01-30", "%Y-%m-%d"):
	# if sample_date == date.today():
            print str(sample_date)
	    statx = {}
	    statx['meta'] = {}
	    statx['meta']['host_id'] = s['metadata']['node']
	    statx['meta']['date'] = sample_date
	    statx['stat'] = {}
	    statx['stat']['stat_name'] = s['meter']
	    statx['stat']['value'] = s['volume']
	    statx['stat']['unit'] = s['unit']
	    stats['sample_stat'].append(statx)
        else:
            print str(date.today())
    return stats


# Serialize pairs of stats from Ceilometer
# Put serialized stats into autoscheduler_db
def save_stats(stats):
    pprint.pprint(stats)
    db = db_connector.connect_to_db()
    collection = db_connector.get_collection(collection_name='hosts_statistics', db=db)
    serialized_stats = {}
    for s in stats:
        db_connector.add_document(collection=collection, query=s)


token = helpers.openstack_auth()
stats = get_stats(token=token)
save_stats(stats)

