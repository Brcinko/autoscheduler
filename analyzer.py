"""
    analyzer, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import WEIGHTS_DICTIONARY
import db_connector

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
    query= '{ \'meta.doc_definition\': {$nin: True}}'
    collection = db_connector.get_collection(db=db, collection_name='hosts_statistics')
    documents = db_connector.get_documents(collection=collection, query=query)

    for h in hosts_list:
        pass
    return test_input


def compute_variance():
    pass


def compute_multiplicator():
    pass
