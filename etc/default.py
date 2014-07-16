#!/usr/bin/env python

import os
import sys

cwd = os.path.dirname(os.path.abspath(__file__))

monitor_dir = "/home/vsftpd"
efile_name = "readme.txt"  
layer_num = 3
used_task_file = "/tmp/dam_used_task.txt"

mail_switch = True
mail_sub = "ReMatch New Task"
mail_from = "dam_service@vobile.net"
mail_server = "mail.vobile.cn"
mail_type = "html"
mail_to = ["yu_ronghua@vobile.cn"]
TIME_FORMAT = '%Y-%m-%d %H:%M:%S' # for mail

request_switch = True
request_host = "localhost"
request_port = 8080

component = "auto_commit"
LOGGING_CONF = cwd + "/logging_config.conf"
import logging.config
logging.config.fileConfig(LOGGING_CONF)
import logging
logger = logging.getLogger(component)
