"""
    stats_collector, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

import pymongo
import db_connector
import settings


# Get stats from Ceilometer
# Match stats for meters and ISODate
def get_stats():
    stats = {}
    return stats


# Serialize pairs of stats from Ceilometer
# Put serialized stats into autoscheduler_db
def save_stats(stats):
    db = db_connector.connect_to_db()
    collection = db_connector.get_collection(collection_name='hosts_statistics', db=db)
    serialized_stats = {}
    for s in stats:
        db_connector.add_document(collection=collection, query=s)


get_stats()
save_stats()
