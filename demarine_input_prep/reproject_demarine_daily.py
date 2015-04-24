__author__ = 'carole'

from sys import argv
from os import  makedirs, system
from os.path import exists
from demarine_input_prep.demarine_conf import gptProcessor, DeMarine_fine_grid_graph_file, \
    DeMarine_coarse_grid_graph_file
from conf.utilities import getDOY, ensureTrailingSlash
from demarine_input_prep.demarine_paths import modisL3_TSMBasePath, modisL3_TSMDemarine_CoarseGrid_Path, \
    modisL3_TSMDemarine_FineGrid_Path


def printUsage():
    print("Usage: ", argv[0], "<date>")
    print("where date is a string representing the date to process,")
    print("e.g. 20120607 for June 7, 2012.")


if len(argv) != 2:
    printUsage()
    exit(1)

back_date = argv[1]
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
modisL3_DeM_FinePath = ensureTrailingSlash(modisL3_TSMDemarine_FineGrid_Path)
modisL3_DeM_CoarsePath = ensureTrailingSlash(modisL3_TSMDemarine_CoarseGrid_Path)

for _path in [modisL3_DeM_FinePath]:
    if not exists(_path):
        print("Making directory: ", _path, " ...")
        makedirs(_path)

for _path in [modisL3_DeM_CoarsePath]:
    if not exists(_path):
        print("Making directory: ", _path, " ...")
        makedirs(_path)
# try:
# srcList = listdir(modisL3_TSMPath)
# except OSError:
#     print("Cannot open ", modisL3_TSMPath+ "! Now exiting...")
#     exit(1)
# else:
#     listSize = exit_on_empty_list(srcList)
#     print(listSize)
#
# # Liste bereinigen:
# for a in range(listSize):
#     for item in srcList:
#         # if not item.startswith('MODISA_DeM_' + back_date) or not item.endswith('.dim'):
#         if not item.startswith('L3_'+ _year + '-' + _month + '-' + _day) or not item.endswith('.nc'):
#             srcList.remove(item)
#         # if not item.startswith('NorthSea_' + back_date) or not item.endswith('.dim'):
#         #     srcList.remove(item)
#
# listSize = exit_on_empty_list(srcList)
# srcList.sort()
# L3_2008-01-01_2008-01-01
# source_file = 'L3_' + _year + '-' + _month + '-' + _day + '_' + _year + '-' + _month + '-' + _day + '.nc'
source_file = 'L3_' + _year + '-' + _month + '-' + _day + '_' + _year + '-' + _month + '-' + _day + '.nc'

# outputProductPath = modisL3_ECOHAMPath + 'cb_ns_' + back_date + '_eo_bc_lat_lon_ecoham.dim'
outputProductFinePath = modisL3_DeM_FinePath + 'reprojected_DeMarine_' + back_date + '_fine_grid.dim'
outputProductCoarsePath = modisL3_DeM_CoarsePath + 'reprojected_DeMarine_' + back_date + '_coarse_grid.dim'



reproj_fine_processingCall = gptProcessor + ' ' + DeMarine_fine_grid_graph_file + ' -Ssource=' + modisL3_TSMPath + source_file + ' -Pfile=' + outputProductFinePath
system(reproj_fine_processingCall)
reproj_coarse_processingCall = gptProcessor + ' ' + DeMarine_coarse_grid_graph_file + ' -Ssource=' + modisL3_TSMPath + source_file + ' -Pfile=' + outputProductCoarsePath
system(reproj_coarse_processingCall)
# print(srcList, outputProductFinePath, outputProductCoarsePath)


