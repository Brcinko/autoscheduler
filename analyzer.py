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
    pprint.pprint(documents)
    response = {}
    response['filters'] = []
    response['weights'] = []
    # ------------------WEIGHT ANALYSIS------------------------
    for w in WEIGHTS_DICTIONARY:
        hosts_variance = []
        for h in hosts_list:
            host_stats_list = []
            for d in documents:
                # if stats are from this very host
                if h == d['meta']['host_id']:
                    for s in d['stats']:
                        # TODO .used and .average in stats are NOT the same - some distinguisher must be provide
                        if w['stat_name'] in s['stat_name']:
                            # missing same unit check
                            host_stats_list.append(s['stat_value'])
            variance = compute_variance(stats=host_stats_list)
            hosts_variance.append(variance)
        multiplicator = compute_multiplicator(variances=hosts_variance)
        # append new weight into response
        weightx = {}
        weightx['weight_name'] = w['weight_name']
        weightx['weight_value'] = multiplicator
        response['weights'].append(weightx)

    # -------------FILTER ANALYSIS-----------------------------
    response['filters'] = DEFAULT_FILTERS
    pprint.pprint(response)
    return test_input


# sem poslem list nameranych hodnot a vypocita to odchylku
def compute_variance(stats):
    return 2.5


# sem poslem odchylku kazdeho stroja a vypocyta to vyslednu vahu
def compute_multiplicator(variances):
    return 2.0
