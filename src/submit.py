#!/usr/bin/env python

import os
import sys
import commands

from etc import common as config
logger = config.logger

#Sent request to DAMService
def send_request(*args, **kwargs):
    task_folder = args[0]
    if not os.path.exists(task_folder):
        logger.error(task_folder + " is not exists.")
        raise Exception("Task is not exists.")
    path_split = task_folder.split('/')
    user_name = path_split[-2]
    curl_cmd = '''curl -H"Content-Type:application/json" -d'{"user_name":"%s","storage_uri":"%s",\
"sid":"a3b7f53fafb970300a48dee7a1af1eb0"}' "%s:%s/service/backdoor/load/task"''' \
%(user_name, task_folder, config.request_host, config.request_port)
    logger.info("send request: %s" %curl_cmd)
    status, output = commands.getstatusoutput(curl_cmd)
    logger.info("status: %s, output: %s" %(status, output))
    if status != 0 or output[-7:].upper() != 'SUCCESS':
        msg = "send request failed " + str(status) + output
        logger.error(msg)
        raise Exception(msg)
    return True

if __name__ == '__main__':
    try:
        send_request("/home/vsftpd/oqm/task1")
    except Exception, e:
        print e
