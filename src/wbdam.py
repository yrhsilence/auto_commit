#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import pyinotify

import daemon
import function
from mail import send_mail
from submit import send_request

sys.path.append("..")
from etc import wbdam as config
logger = config.logger

def trim_boundary_slash(path):
    if path[0] == os.path.sep: path = path[1:]
    if path[-1] == os.path.sep: path = path[0:-1]
    return path

def exclude_filter(path):
    if (os.path.basename(path) != config.efile_name):
        return False

    base_path = trim_boundary_slash(config.monitor_dir)
    path = trim_boundary_slash(path) 
    if (len(path.split(os.path.sep)) - len(base_path.split(os.path.sep)) != config.layer_num):
        return False
    return True

def process_create(pathname):
    try:
        logger.info("process task: " + pathname)
        target_path = os.path.join(config.sync_target_dir, os.path.basename(pathname))
        if function.is_folder_not_used(target_path): 
            if (os.path.exists(target_path)):
                os.unlink(target_path)
            os.symlink(pathname, target_path)
            logger.info("link: " + pathname + " to " + target_path)
            send_request(target_path)
            send_mail(target_path, 'success', 'Process success')
            function.write_task_record(target_path)
            logger.info(target_path + " process success!")
        else:
            logger.error(target_path + " is used!")
            send_mail(target_path, "warning", "Task has used")
    except Exception, e:
        logger.error(e)
        send_mail(target_path, "failed", e)

def process_modify(pathname):
    send_mail(pathname, "success", "modify")


class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        #logger.info("Creating task: " + event.pathname)
        if (exclude_filter(event.pathname)):
            logger.info("Creating task: " + event.pathname)
            process_create(os.path.split(event.pathname)[0])

    def process_IN_MODIFY(self, event):
        if (event.name == config.efile_name):
            logger.info("Motify task: " + event.pathname)
            process_modify(os.path.split(event.pathname)[0])

def monitor(monitor_dir = None):
    if (monitor_dir == None):
        monitor_dir = config.monitor_dir
    logger.info("wbdam monitor_dir: " + monitor_dir)
    wm = pyinotify.WatchManager()  # Watch Manager
    mask = pyinotify.IN_CREATE | pyinotify.IN_MODIFY  # watched events
    notifier = pyinotify.Notifier(wm, EventHandler())
    wdd = wm.add_watch(monitor_dir, mask, rec = True, auto_add = True)

    notifier.loop()

if __name__ == "__main__":
    with daemon.DaemonContext():
        monitor()
