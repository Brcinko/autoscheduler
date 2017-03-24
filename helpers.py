"""
    helpers, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

import datetime
import pprint

hosts_list = {
    "hosts": [
        {
            "host_name": "host-01",
            "service": "conductor",
            "zone": "internal"
        },
        {
            "host_name": "host-02",
            "service": "compute",
            "zone": "nova"
        },
        {
            "host_name": "backup-host",
            "service": "consoleauth",
            "zone": "internal"
        },
        {
            "host_name": "396a8a0a234f476eb05fb9fbc5802ba7",
            "service": "network",
            "zone": "internal"
        },
        {
            "host_name": "abffda96592c4eacaf4111c28fddee17",
            "service": "scheduler",
            "zone": "internal"
        }
    ]
}


def create_conf_doc(doc_definition, configurations):
    # pprint.pprint(doc_definition[0]['settings'][0]['filter_name'])
    document = {}
    # metadata
    document['meta'] = {}
    document['meta']['date'] = datetime.datetime.utcnow()
    document['meta']['doc_version'] = doc_definition[0]['meta']['doc_version']
    # settings - filters
    document['settings'] = []
    for d in doc_definition[0]['settings']:
        if d['filter_name'] in configurations['filters']:
            # print d['filter_name']
            documentx = {}
            documentx['conf_status'] = 'on'
            documentx['filter_name'] = d['filter_name']
            document['settings'].append(documentx)
        else:
            documentx = {}
            documentx['conf_status'] = 'off'
            documentx['filter_name'] = d['filter_name']
            document['settings'].append(documentx)
    # pprint.pprint(document)
    return document


def create_hosts_list_doc(doc_definition, hosts_list):
    document = {}
    # metadata
    document['meta'] = {}
    document['meta']['date'] = datetime.datetime.utcnow()
    document['meta']['doc_version'] = doc_definition[0]['meta']['doc_version']
    # hosts
    document['hosts'] = []
    for h in hosts_list['hosts']:
        hostx = {}
        hostx['host_name'] = h
        document['hosts']. append(hostx)
    # pprint.pprint(document)
    return document


# get list of physical servers from OpenStack
def get_host_list():
    # possible way, with following command
    # https://ask.openstack.org/en/question/67928/list-of-available-hosts/

    # other way - API call GET /os-hosts
    # https://developer.openstack.org/api-ref/compute/?expanded=list-hosts-detail

    hosts = {}
    hosts['hosts'] = []
    for h in hosts_list['hosts']:
        hosts['hosts'].append(h['host_name'])

    # unique list records - first option has a duplicated values
    hosts['hosts'] = list(set(hosts['hosts']))
    return hosts


def create_stat_doc(stat):
    pass
