"""
    scheduler-configurator, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""
from settings import NOVA_CONF_FILE

test_input = {
    'filters': ['RamFilter', 'DiskFilter', 'ComputeFilter']
}


def set_config(config_request):
    conf_line = create_config_line(test_input['filters'])
    print conf_line
    file = read_conf_file()
    for f in file:
        if f[:25] == 'scheduler_default_filters':
            print f


def create_config_line(filters):
    config_string = 'scheduler_default_filters = '
    i = 0
    for f in filters:
        if i == 0:
            config_string += f
        else:
            config_string += ', '
            config_string += f
        i +=1
    return config_string


def read_conf_file():
    with open(NOVA_CONF_FILE) as f:
        content = f.readlines()
    # print content
    return content

set_config("")