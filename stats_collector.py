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


# ------method for getting memory info from files-----
def get_memory_stats():

    with open('memory1.txt') as data:
        d = data.read()
        d = eval(d)
    with open('memory2.txt') as data:
        c = data.read()
        c = eval(c)

    d += c
    response = []
        
    for r in d:
        sample_date = datetime.datetime.strptime(str(r['meta']['date'])[:10], "%Y-%m-%d")
        if str(sample_date)[:10] == str(datetime.date.today()):
            response.append(r)
            print "PRIDAVAM"
            pprint.pprint(r)
    return response


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
        sample_date = datetime.datetime.strptime(s['timestamp'][:10], "%Y-%m-%d")
        if sample_date == datetime.datetime.strptime("2014-01-30", "%Y-%m-%d"):
        # if sample_date == datetime.date.today():
            # print str(sample_date)
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
            pass
            # print str(datetime.date.today())
    # workaround of not working hardware.memory sensor
    if settings.MEMORY_FROM_FILE is True:
        print "PRVY"
        response = get_memory_stats()
        # print response
        stats['sample_stat'] += response
    # print stats
    return stats


token = helpers.openstack_auth()
stats = get_stats(token=token)


"""
get_stats RESPONSE EXAMPLE

{'sample_stat': [{'meta': {'date': datetime.datetime(2017, 1, 30, 0, 0),
                           'host_id': u'oscompute-1'},
                  'stat': {'stat_name': u'disk.ephemeral.size',
                           'unit': u'GB',
                           'value': 0.0}},
                 {'meta': {'date': datetime.datetime(2017, 1, 30, 0, 0),
                           'host_id': u'oscompute-1'},
                  'stat': {'stat_name': u'disk.ephemeral.size',
                           'unit': u'GB',
                           'value': 0.0}}]}

"""

