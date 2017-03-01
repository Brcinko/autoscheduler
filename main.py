"""
    main modul, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import NOVA_CONF_FILE
from scheduler_configurator import set_config
import helpers
import pprint


config = {
    'settings': [
        {
            "filter_name": "RamFilter",
            "conf_status": "on"
        },
        {
            "filter_name": "CoreFiler",
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
            "filter_name": "ComputeFiler",
            "conf_status": "on"
        },
        {
            "filter_name": "JSONFilter",
            "conf_status": "on"
        }
    ]
}


def auto_scheduling():
    # TODO module from statistic analyze
    set_config()
    update_config_db()


def update_config_db():
    helpers.create_conf_doc()
