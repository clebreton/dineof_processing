__author__ = 'carole'

from sys import argv
from os import makedirs, system
from os.path import exists
from demarine_input_prep.demarine_conf import gptProcessor, subset_graph_file
from conf.utilities import getDOY, ensureTrailingSlash
from demarine_input_prep.demarine_paths import modisL3_TSMBasePath
from conf.paths import intermediate_Dir
from pathlib import Path, PurePath
from glob import glob

def printUsage():
    print("Usage: ", argv[0], "<date>")
    print("where date is a string representing the date to process,")
    print("e.g. 20120607 for June 7, 2012.")

def subset(back_date):
    if len(back_date) != 8:
        print("****************************")
        print("* date parameter malformed *")
        print("****************************")
        printUsage()
        exit(1)

# digidi
if __name__ == '__main__':
    argc = len(argv)
    if argc < 2:
        printUsage()
    else:
        back_date = argv[1]
        procYear = back_date[:4]
        procMonth = back_date[4:6]
        procDay = back_date[6:]
        print("Processing date: ", back_date)
        # exit(1)

        modisL3_TSMPath = ensureTrailingSlash(modisL3_TSMBasePath)
        modisL3_SubsetPath = ensureTrailingSlash(intermediate_Dir)

        for _path in [modisL3_SubsetPath]:
            if not exists(_path):
                print("Making directory: ", _path, " ...")
                makedirs(_path)

        source_list = glob(modisL3_TSMBasePath + '*' + procYear + '-' + procMonth + '-' + procDay + '_' + procYear + '-' + procMonth + '-' + procDay + '*')

        if source_list:
            source_file = source_list[0]
            _sp = source_file
            outputFileName = PurePath(_sp).stem + '_subset.dim'
            processingCall = gptProcessor + ' ' + subset_graph_file + ' -Ssource=' + _sp + ' -Pfile=' + modisL3_SubsetPath + outputFileName
            system(processingCall)
        else:
            print("No source file found. Exiting now...")
            exit(1)




