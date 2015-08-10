#!/usr/bin/env python3
__author__ = 'uwe'

from os import system, chdir
from sys import argv, exit
from conf.paths import trigger_dir
from conf.utilities import getBackDateStr
from pathlib import Path
from demarine_input_prep.demarine_paths import modisL3_TSMBasePath
from glob import glob

def printUsage():
    print("Usage: ", argv[0], " backDay")
    print("where backDay is the number of days before today")
    print("e.g. 1 means yesterday etc...\n")
    exit(1)

if __name__ == '__main__':
    argc = len(argv)
    if argc < 2:
        printUsage()
    else:
        backDay = argv[1]
        procDate = getBackDateStr(int(backDay))
        procYear = procDate[:4]
        procMonth = procDate[4:6]
        procDay = procDate[6:]
        print("Processing date: ", procDate)
        # exit(1)

    trigger_lock = trigger_dir + procDate
    _tp = Path(trigger_lock)
    source_list = glob(modisL3_TSMBasePath + '*' + procYear + '-' + procMonth + '-' + procDay + '_' + procYear + '-' + procMonth + '-' + procDay + '*')
    print(source_list)
    if source_list:
        source_file = source_list[0]
    _sp = Path(source_file)
    print(procDate, procYear, procMonth, procDay, _sp, _sp.exists())
    # exit(1)

    if _sp.exists() and not _tp.exists():
        print("New source file found. Starting DINEOF processing...")
        _tp.touch() # Avoid multiple processings through crontab
        # Processing part comes here
        syscall = "/bin/bash -c \"export PYTHONPATH=/data/carole/dineof_processing; " \
                  "python3 /data/carole/dineof_processing/control/processDINEOF.py " + procDate + "\""
        print("Executing: ", syscall)
        system(syscall)
    else:
        print("\nNo new source file found. Nothing to do.\n")
        exit(1)
#TODO make break types clearer
