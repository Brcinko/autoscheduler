# Nova settings
NOVA_ADDRESS = "http://oscore.cloud.ngnlab.eu:8774/v2"
NOVA_HOST_LIST_ROUTE = '/os-hosts'

# nova-scheduler setting #
NOVA_CONF_FILE = "/etc/nova/nova.conf"
FILTERS_CONFIG_LINE = "scheduler_default_filters = "
WEIGHT_CONFIG_LINE = "scheduler_weight_classes = nova.scheduler.weights.all_weighers\n"
WEIGHT_TYPE_STRING = "_multiplier = "
ALLOWED_WEIGHTS = ['io_ops_weight', 'ram_weight']
WEIGHTS_DICTIONARY = [
    {
        'weight_name': 'ram_weight',
        'stats_name': 'hardware.memory'
    },
    {
        'weight_name':  'io_ops_weight',
        'stats_name': 'hardware.system_stats.io'
    }
]

DEFAULT_FILTERS = ['CoreFilter', 'ComputeFilter', 'RamFilter']


# Database settings #
DB_PORT = 27017
DB_ADDRESS = "localhost"


# Ceilometer settings #
CEILOEMETER_ADDRESS = "http://oscore.cloud.ngnlab.eu:8777"
CEILOMETER_SAMPLE_ROUTE = "/v2/samples?limit=5"
KEYSTONE_ADDRESS = "http://oscore.cloud.ngnlab.eu:5000/v2.0"
KEYSTONE_TOKEN_ROUTE = '/tokens'