"""
    analyzer, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import WEIGHTS_DICTIONARY, DEFAULT_FILTERS
import db_connector
import pprint
import math

test_input = {
    'filters': ['CoreFilter', 'IoOpsFilter', 'RamFilter'],
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
    query['meta.definition'] = {}
    query['meta.definition']['$nin'] = [True]
    collection = db_connector.get_collection(db=db, collection_name='hosts_statistics')
    documents = db_connector.get_documents(collection=collection, query=query)
    response = {}
    response['filters'] = []
    response['weights'] = []
    stat_name = ""
    multiplicators = []
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
                        # TODO WARNING .total is in production not .average!!!!
                        # pprint.pprint(s)
                        stat_name = w['stats_name'] + ".used"
                        if stat_name in s['stat_name']:
                            #missing same unit check
                            # pprint.pprint(s['stat_name'])
                            host_stats_list.append(float(s['value']))

                        breakpoint_name = s['stat_name'] = w['stats_name'] + ".average"
                        if breakpoint_name in s['stat_name']:
                            value = s['value'].replace(",", ".")
                            breakpoint = float(value) * 0.1



            # pprint.pprint(host_stats_list)
            variance = compute_variance(stats=host_stats_list)
            # print variance
            hosts_variance.append(variance)
        # pprint.pprint(hosts_variance)
        multiplicatorx = compute_multiplicator(variances=hosts_variance, breakpoint=breakpoint)
        pprint.pprint(multiplicatorx)
        multiplicator = get_max_weight(weight_list=multiplicatorx)
        print multiplicator
        multiplicators.append(multiplicator)
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
    i = None
    if len(stats) > 0:
        average = sum(stats) / len(stats)
        # print average
        i = 0
        for s in stats:
            i += abs((s - average)*(s - average))
        i = i / len(stats)
        i = math.sqrt(i)
        # print i
    return i


# sem poslem odchylku stroja a hranicnu hodnotu a vypocitam multiplicator pre stroj
def compute_multiplicator(variances, breakpoint):
    weight_list = []
    i = 0
    for v in variances:
        if v is not None:
            # TODO remove *10
            v = v * 10
            if v <= breakpoint:
                i = 1.0
            elif breakpoint > v <= (breakpoint * 2):
                i = 1.5
            elif (breakpoint * 2) > v <= (breakpoint * 3):
                i = 2
            elif (breakpoint *3) > v <=(breakpoint * 4):
                i = 2.5
            elif v > (breakpoint * 4):
                i = 3
            weight_list.append(i)
    return weight_list


def get_max_weight(weight_list):
    if weight_list:
        return max(weight_list)
    pass

