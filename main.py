"""
    main modul, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import NOVA_CONF_FILE
from scheduler_configurator import set_config
import db_connector
import helpers
import pprint

# response from data analysis should be in this format
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


def auto_scheduling():
    # connect to DB
    db = db_connector.connect_to_db()

    # get host list from OpenStack
    host_list = helpers.get_host_list()
    pprint.pprint(host_list)
    update_hosts_list_db(db=db, host_list=host_list)

    # TODO module from statistic analyze

    set_config(test_input)
    update_config_db(db=db)


def update_config_db(db):
    # Get collection
    collection = db_connector.get_collection(collection_name='configurations', db=db)
    # Get 'configurations' document definition
    query = {}
    query['meta.definition'] = True
    query['meta.doc_version'] = -1  # DESCENDING ORDERING
    doc_definition = db_connector.get_sorted_documents(collection=collection, query=query)
    # Create document
    # TODO toto zmenit na produkciu
    conf = test_input
    doc = helpers.create_conf_doc(doc_definition=doc_definition, configurations=conf)
    # insert into DB
    db_connector.add_document(collection=collection, query=doc)


def update_hosts_list_db(db, host_list):
    # Get collection
    collection = db_connector.get_collection(collection_name='hosts_list', db=db)
    # Get 'configurations' document definition
    query = {}
    query['meta.definition'] = True
    query['meta.doc_version'] = -1  # DESCENDING ORDERING
    doc_definition = db_connector.get_sorted_documents(collection=collection, query=query)
    doc = helpers.create_hosts_list_doc(doc_definition=doc_definition, hosts_list=host_list)
    # insert into DB
    db_connector.add_document(collection=collection, query=doc)

auto_scheduling()
