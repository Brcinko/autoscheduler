"""
    helpers, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

import datetime
import pprint


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
            print d['filter_name']
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