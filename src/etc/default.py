#!/usr/bin/env python

import os
import sys

from common import logger

monitor_dir = "/home/vsftpd"
efile_name = "readme.txt"  
layer_num = 3

mail_switch = True
mail_sub = "ReMatch New Task"
mail_from = "yrhsilence@126.com"
mail_server = "mail.126.com"
mail_type = "html"
mail_to = ["yrhsilence@126.cn"]
TIME_FORMAT = '%Y-%m-%d %H:%M:%S' # for mail

request_switch = True
request_host = "localhost"
request_port = 8080
