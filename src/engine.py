#!/usr/bin/env python

import os
import sys
import subprocess

import daemon
from default import monitor as default_monitor
from wbdam import monitor as wbdam_monitor

from etc import default as config
logger = config.logger

CWD = os.path.dirname(__file__)

def write_pid(p_list):
    pid_file = os.path.join(CWD, "../run/pid")
    fp = open(pid_file, "w")
    for item in p_list:
        fp.write(str(item) + " ")

def monitor():
    try:
        p_list = []
        cmd = []
        cmd.append("python")
        cmd.append(os.path.join(CWD, "default.py"))
        pdefault = subprocess.Popen(cmd)
        p_list.append(pdefault.pid)

        cmd = []
        cmd.append("python")
        cmd.append(os.path.join(CWD, "wbdam.py"))
        pwbdam = subprocess.Popen(cmd)
        p_list.append(pwbdam.pid)
        
        logger.info("pid: %s" %p_list)
        write_pid(p_list)

        cmd = [] 
        cmd.append(os.path.join(CWD, "auto_commit_watchdog"))
        cmd.append("2")
        subprocess.Popen(cmd)
    except Exception, e:
        logger.error(e)

if __name__ == "__main__":
    monitor()
