# nova-scheduler setting #
NOVA_CONF_FILE = "/etc/nova/nova.conf"
FILTERS_CONFIG_LINE = "scheduler_default_filters = "
WEIGHT_CONFIG_LINE = "scheduler_weight_classes = nova.scheduler.weights.all_weighers\n"
WEIGHT_TYPE_STRING = "_multiplier = "

# Database settings #
DB_PORT = 27017
DB_ADDRESS = "localhost"