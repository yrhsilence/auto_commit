#!/usr/bin/env python

import os
import sys
import subprocess

import daemon

from etc import common as config
logger = config.logger

CWD = os.path.dirname(__file__)

def write_pid(p_list):
    pid_file = os.path.join(CWD, "../run/pid")
    fp = open(pid_file, "w")
    for item in p_list:
        fp.write(str(item) + " ")

def monitor():
    try:
        # Process the tasks
        task_list = config.TASK_LIST
        p_list = []
        for task in task_list:
            cmd = []
            cmd.append("python")
            cmd.append(os.path.join(CWD, task))
            pdefault = subprocess.Popen(cmd)
            p_list.append(pdefault.pid)
        
        logger.info("pid: %s" %p_list)
        write_pid(p_list)

        # Start watchdog to monitor pids.
        cmd = [] 
        cmd.append("bash")
        cmd.append(os.path.join(CWD, "auto_commit_watchdog"))
        cmd.append(str(len(task_list)))
        subprocess.Popen(cmd)
    except Exception, e:
        logger.error(e)

if __name__ == "__main__":
    monitor()
