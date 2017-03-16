"""
    analyzer, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import WEIGHTS_DICTIONARY, DEFAULT_FILTERS
import db_connector
import pprint

test_input = {
    'filters': ['CoreFilter', 'ComputeFilter', 'RamFilter'],
    'weights': [
        {
            'weight_name': 'ram_weight',
            'weight_value': 1.0
        },
        {
            'weight_name': 'io_ops_weight',
            'weight_value': 1.0
        }
    ]
}


def analyze_stats(db, hosts_list):
    # get stats
    # query = '{ \'meta.doc_definition\': {$nin: True}}'
    query = {}
    query['meta.doc_definition'] = {}
    query['meta.doc_definition']['$nin'] = [True]
    collection = db_connector.get_collection(db=db, collection_name='hosts_statistics')
    documents = db_connector.get_documents(collection=collection, query=query)
    response = {}
    response['filters'] = []
    response['weights'] = []
    # ------------------WEIGHT ANALYSIS------------------------
    for w in WEIGHTS_DICTIONARY:
        # pprint.pprint(w)
        hosts_variance = []
        for h in hosts_list['hosts']:
            host_stats_list = []
            for d in documents:
                # if stats are from this very host
                # pprint.pprint(h)
                if h == d['meta']['host_id']:
                    for s in d['stats']:
                        # TODO .used and .average in stats are NOT the same - some distinguisher must be provide
                        # pprint.pprint(s)
                        if w['stats_name'] in s['stat_name']:
                            #missing same unit check
                            # pprint.pprint(s['stat_name'])
                            host_stats_list.append(float(s['value']))
            pprint.pprint(host_stats_list)
            variance = compute_variance(stats=host_stats_list)
            hosts_variance.append(variance)
        pprint.pprint(hosts_variance)
        multiplicator = compute_multiplicator(variances=hosts_variance)
        # append new weight into response
        weightx = {}
        weightx['weight_name'] = w['weight_name']
        weightx['weight_value'] = multiplicator
        response['weights'].append(weightx)

    # -------------FILTER ANALYSIS-----------------------------
    response['filters'] = DEFAULT_FILTERS
    # pprint.pprint(response)
    return response


# sem poslem list nameranych hodnot a vypocita to odchylku
def compute_variance(stats):
    return 2.5


# sem poslem odchylku kazdeho stroja a vypocyta to vyslednu vahu
def compute_multiplicator(variances):
    i = 0
    for v in variances:
        if v >= 1.0 and v <= 2.5:
            i += 0.5
        elif 2.5 > v <= 3.5:
            i += 1
        elif 3.5 > v:
            i += 1.5
    return i
