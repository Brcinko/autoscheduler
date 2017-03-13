"""
    scheduler-configurator, author: Lukas Klescinec <lukas.klescinec@gmail.com>
    FIIT Slovak University of Technology 2017
    This module is part of master thesis.
"""
from settings import NOVA_CONF_FILE, FILTERS_CONFIG_LINE, WEIGHT_CONFIG_LINE, WEIGHT_TYPE_STRING, ALLOWED_WEIGHTS
import pprint


def set_config(config_request):
    filter_conf_line = create_filter_config_lines(config_request['filters'])
    weight_conf_line = create_weights_config_lines(config_request['weights'])
    file = read_conf_file()
    validation_result = config_file_validation(file)
    # print str(validation_result)

    # TODO chceck if weights position is higher than filter position
    for v in validation_result['weights']['weights_type']:
        del(file[v['position']])


    if validation_result['filters']['empty_filters'] is True:
        # scheduler_default_filters line is missing
        file.insert(validation_result['filters']['position'], filter_conf_line)
    else:
        # scheduler_default_filters line is present
        file[validation_result['filters']['position']] = filter_conf_line
    if validation_result['weights']['empty_weights'] is True:
        file.insert(validation_result['weights']['position'], weight_conf_line)
    else:
        file[validation_result['weights']['position']] = weight_conf_line

    write_into_conf_file(file)



def create_filter_config_lines(filters):
    config_string = FILTERS_CONFIG_LINE
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


def create_weights_config_lines(weights):
    config_string = WEIGHT_CONFIG_LINE
    for w in weights:
        config_string += w['weight_name'] + WEIGHT_TYPE_STRING + str(w['weight_value']) + '\n'
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

    # -----------------FilterScheduler Validator--------------------------------
    validation = {}
    validation['filters'] = {}
    empty_filters_flag = True
    i = 0
    for f in file:
        # TODO switch to settings.py
        if f[:25] == 'scheduler_default_filters':
            empty_filters_flag = False
            break
        i += 1
        empty_filters_flag = True
    # if filter configuration line is missing find position for this config line
    if empty_filters_flag is True:
        i = 0
        for f in file:
            # right side of condition is not working, i am fine with that
            if f[:9] == 'scheduler' and ('scheduler' not in file[i+1] or '#' not in file[i+1]):
                 break
            i += 1
    validation['filters']['empty_filters'] = empty_filters_flag
    validation['filters']['position'] = i

    # ---------------Weight Configuration Validator-----------------------------------
    # TODO this validation
    i = 0
    validation['weights'] = {}
    for f in file:
        if f[:64] == WEIGHT_CONFIG_LINE:
            empty_filters_flag = False
            break
        i += 1
        empty_filters_flag = True
    # if filter configuration line is missing find position for this config line
    if empty_filters_flag is True:
        i = 0
        for f in file:
            # right side of condition is not working, i am fine with that
            if f[:9] == 'scheduler' and ('scheduler' not in file[i+1] or '#' not in file[i+1]):
                 break
            i += 1
    validation['weights']['empty_weights'] = empty_filters_flag
    validation['weights']['position'] = i
    # --Weight multiplicators validation--

    validation['weights']['weights_type'] = []
    for w in ALLOWED_WEIGHTS:
        weight = str(w) + WEIGHT_TYPE_STRING
        i = 0
        for f in file:
            wx = {}
            if weight in f:
                wx['weight_type_name'] = weight
                wx['position'] = i
                validation['weights']['weights_type'].append(wx)
            i += 1

    # pprint.pprint(validation)
    return validation
