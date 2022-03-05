#!/usr/bin/python3

import sys
from pyrob.api import run_tasks

import task_14
import task_15
import task_19
import task_23
import task_26
import task_29


if __name__ == '__main__':
    res = run_tasks(headless=True)
    sys.exit(0 if res else -1)
