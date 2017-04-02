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


# serialize configuration date which are given
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


# return list of active host in cloud
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

    # unique list records - there are duplicated values in response from nova
    hosts['hosts'] = list(set(hosts['hosts']))
    pprint.pprint(hosts)
    return hosts


# Return list of serialized stat documents
def create_stats_docs(stat, host_list, doc_definition):
    documents = []
    for h in host_list['host_list']:
        docx = {}
        docx['stats'] = []
        for s in stat['sample_stat']:
            # db_connector.add_document(collection=collection, query=s)
            if h == s['meta']['host_id']:
                docx['meta'] = {}
                docx['meta']['host_id'] = s['meta']['host_id']
                docx['meta']['date'] = s['meta']['date']
                docx['meta']['doc_version'] = doc_definition['meta']['doc_version']
                statx = {}
                statx['value'] = s['stat']['value']
                statx['stat_name'] = s['stat']['stat_name']
                statx['unit'] = s['stat']['unit']
                docx['stats'].append(statx)
        documents.append(docx)

    return documents


# Modul for athentication with OpenStack which return auth token
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

# get_host_list()
