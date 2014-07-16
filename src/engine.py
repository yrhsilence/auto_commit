#!/usr/bin/env python

import os
import subprocess

import daemon
from default import monitor as default_monitor
from wbdam import monitor as wbdam_monitor

def monitor():
    #cmd = []
    #cmd.append("default.py")
    #subprocess.Popen(cmd)

    #cmd = []
    #cmd.append("wbdam.py")
    #subprocess.Popen(cmd)
    try:
      cmd = "python default.py"
        os.system(cmd)
        
        cmd = "python wbdam.py"
        os.system(cmd)
    except Exception, e:
        print e

if __name__ == "__main__":
    monitor()
