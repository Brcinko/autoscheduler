"""
    helpers, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

import datetime
import pprint
import requests
import settings

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
    # pprint.pprint(doc_definition['settings'])
    document = {}
    # metadata
    document['meta'] = {}
    document['meta']['date'] = datetime.datetime.utcnow()
    document['meta']['doc_version'] = doc_definition['meta']['doc_version']
    # settings - filters
    document['settings'] = {}
    document['settings']['filters'] = []
    document['settings']['weights'] = []
    for d in doc_definition['settings']['filters']:
        if d['filter_name'] in configurations['filters']:
            # print d['filter_name']
            documentx = {}
            documentx['conf_status'] = 'on'
            documentx['filter_name'] = d['filter_name']
            document['settings']['filters'].append(documentx)
        else:
            documentx = {}
            documentx['conf_status'] = 'off'
            documentx['filter_name'] = d['filter_name']
            document['settings']['filters'].append(documentx)
    for d in configurations['weights']:
        documentx = {}
        documentx['weight_name'] = d['weight_name']
        documentx['weight_status'] = 'on'
        documentx['weight_value'] = d['weight_value']
        document['settings']['weights'].append(documentx)
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
    # GET auth credentials
    token = openstack_auth()
    header = {"X-Auth-Token": token}
    uri = settings.NOVA_ADDRESS + '/' + settings.TENANT_ID + settings.NOVA_HOST_LIST_ROUTE
    r = requests.get(uri, headers=header)
    response = r.json()
    pprint.pprint(response)
    hosts = {}
    hosts['hosts'] = []
    for h in response['hosts']:
        hosts['hosts'].append(h['host_name'])

    # unique list records - first option has a duplicated values
    hosts['hosts'] = list(set(hosts['hosts']))
    pprint.pprint(hosts)
    return hosts


def create_stat_doc(stat):
    pass


def openstack_auth():
    r = requests.post(settings.KEYSTONE_ADDRESS)
    # pprint.pprint(r.text)
    uri = settings.KEYSTONE_ADDRESS + settings.KEYSTONE_TOKEN_ROUTE
    r = requests.post(uri,
                      data='{"auth": {"tenantName": "netcell-testing", "passwordCredentials": {"username":"admin", "password":"TATKO"}}}')
    # pprint.pprint(r.text)
    response = r.json()
    token = response['access']['token']['id']
    return token

get_host_list()
