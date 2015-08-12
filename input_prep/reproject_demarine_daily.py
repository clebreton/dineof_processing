__author__ = 'carole'

from sys import argv
from os import makedirs, system
from os.path import exists
from input_prep.demarine_conf import gptProcessor, DeMarine_coarse_grid_graph_file
from conf.utilities import getDOY, ensureTrailingSlash
from input_prep.demarine_paths import modisL3_TSMBasePath, modisL3_TSMDemarine_CoarseGrid_Path

def printUsage():
    print("Usage: ", argv[0], "<date>")
    print("where date is a string representing the date to process,")
    print("e.g. 20120607 for June 7, 2012.")

def reproject(back_date):
    if len(back_date) != 8:
        print("****************************")
        print("* date parameter malformed *")
        print("****************************")
        printUsage()
        exit(1)

    _year = back_date[:4]
    _month = back_date[4:6]
    _day = back_date[6:]
    _doy = getDOY(_year, _month, _day)
    print("Processing date " + back_date + " (DOY = " + str(_doy) + ").")

    modisL3_TSMPath = ensureTrailingSlash(modisL3_TSMBasePath)
    modisL3_DeM_CoarsePath = ensureTrailingSlash(modisL3_TSMDemarine_CoarseGrid_Path)

    for _path in [modisL3_DeM_CoarsePath]:
        if not exists(_path):
            print("Making directory: ", _path, " ...")
            makedirs(_path)

    source_file = 'L3_MODISA_BC_' + _year + '-' + _month + '-' + _day + '_' + _year + '-' + _month + '-' + _day + \
                  '_NSBS_2000m_v1.0nrt.nc'

    outputProductCoarsePath = modisL3_DeM_CoarsePath + 'reprojected_DeMarine_' + back_date + '_coarse_grid.dim'

    reproj_coarse_processingCall = gptProcessor + ' ' + DeMarine_coarse_grid_graph_file + ' -Ssource=' + modisL3_TSMPath + source_file + ' -Pfile=' + outputProductCoarsePath
    system(reproj_coarse_processingCall)


