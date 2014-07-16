#!/usr/bin/python

import os
import sys
from default import *

monitor_dir = "/home/vsftpd/wbdam/vdna/incoming"
layer_num = 2

sync_switch = True
sync_target_dir = "/home/vsftpd/wbdam"
sync_type = "link" # ["link" | "copy" | "rsync"]

