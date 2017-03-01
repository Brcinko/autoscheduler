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

test_input = {
    'filters': ['CoreFilter', 'ComputeFilter', 'RamFilter']
}

config = {
    'settings': [
        {
            "filter_name": "RamFilter",
            "conf_status": "on"
        },
        {
            "filter_name": "CoreFilter",
            "conf_status": "on"
        },
        {
            "filter_name": "IoOpsFilter",
            "conf_status": "off"
        },
        {
            "filter_name": "DiskFilter",
            "conf_status": "on"
        },
        {
            "filter_name": "ComputeFilter",
            "conf_status": "on"
        },
        {
            "filter_name": "JSONFilter",
            "conf_status": "on"
        }
    ]
}


def auto_scheduling():
    # connect to DB
    db = db_connector.connect_to_db()

    # TODO module from statistic analyze
    set_config(test_input)
    # Get collection
    collection = db_connector.get_collection(collection_name='configurations', db=db)
    # Get 'configurations' document definition
    query = {}
    query['meta.definition'] = True
    doc_definition = db_connector.get_documents(collection=collection, query=query)
    # Create document
    # TODO toto zmenit na produkciu
    conf = test_input
    doc = helpers.create_conf_doc(doc_definition=doc_definition, configurations=conf)
    #insert into DB
    update_config_db(collection, doc)


def update_config_db(collection_name, documet):
    pass

auto_scheduling()
