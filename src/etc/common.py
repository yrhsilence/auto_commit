#!/usr/bin/env python

import os

TASK_LIST = ["wbdam.py", "default.py"]
used_task_file = "/tmp/dam_used_task.txt"

component = "auto_commit"
LOGGING_CONF = "etc/logging_config.conf"

import logging.config
logging.config.fileConfig(LOGGING_CONF)
import logging
logger = logging.getLogger(component)
