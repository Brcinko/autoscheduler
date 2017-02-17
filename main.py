"""
    main modul, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""

from settings import NOVA_CONF_FILE
from scheduler-configurator import set_config()

import pprint


def auto_scheduling():
    # TODO modul from statistic analyze
    set_config()
