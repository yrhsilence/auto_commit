#!/usr/bin/env python

import os
import sys

sys.path.append("..")
from etc import default as config
logger = config.logger

TASK_FILE = config.used_task_file

# Determine whether a task can be performed.
# Return False if a task folder have been record in file
def is_folder_not_used(folder_path):
    used_task_file = TASK_FILE
    open(used_task_file, 'a').close() # If the file is not exist, create it.
    fp = open(used_task_file, 'r+')
    re = filter( lambda x: x.__contains__(folder_path), fp.readlines())
    fp.close()
    return len(re) == 0

# Record task in used_tasks file.
def write_task_record(folder_path):
    used_task_file = TASK_FILE
    fp = open(used_task_file, 'a+')
    fp.write(folder_path + '\n')
    fp.close()

if __name__ == '__main__':
    path = "/tmp/task1"
    if is_folder_not_used(path):
        print "write", path
        write_task_record(path)
