"""
    scheduler-configurator, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""
from settings import NOVA_CONF_FILE

with open(NOVA_CONF_FILE) as f:
    content = f.readlines()
print content