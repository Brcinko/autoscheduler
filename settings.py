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


# Database settings #
DB_PORT = 27017
DB_ADDRESS = "localhost"