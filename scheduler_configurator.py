"""
    scheduler-configurator, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""
from settings import NOVA_CONF_FILE
import pprint

test_input = {
    'filters': ['RamFilter', 'DiskFilter', 'ComputeFilter']
}


def set_config(config_request):
    # pprint.pprint(config_request)
    conf_line = create_config_line(config_request['filters'])
    file = read_conf_file()
    validation_result = config_file_validation(file)
    # print str(validation_result)

    if validation_result['empty_filters'] is True:
        # scheduler_default_filters is missing
        # TODO find position
        file.insert(validation_result['position'], conf_line)
    else:
        # scheduler_default_filters is present
        i = 0
        for f in file:
            if f[:25] == 'scheduler_default_filters':
                file[i] = conf_line
                break
            i += 1
    write_into_conf_file(file)
    # pprint.pprint(file)


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
    config_string += '\n'
    return config_string


def read_conf_file():
    with open(NOVA_CONF_FILE) as f:
        content = f.readlines()
    # print content
    return content


def write_into_conf_file(conf):
    data = open(NOVA_CONF_FILE, "w")
    for c in conf:
        data.write(c)
    data.close()


def config_file_validation(file):
    # TODO IMPORTANT define validation response
    # TODO Validation of mandatory config directives in config file
    # TODO Validation of integration of config file with autoschEDUler
    pass
    validation = {}
    empty_filters_flag = True
    i = 0
    for f in file:
        if f[:25] == 'scheduler_default_filters':
            empty_filters_flag = False
            break
        i += 1
        empty_filters_flag = True
    validation['empty_filters'] = empty_filters_flag
    validation['position'] = i
    return validation
