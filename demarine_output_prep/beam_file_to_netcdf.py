__author__ = 'carole'

'''
creates one netcdf file out of one beam dimap product
created for DeMarine nc exchange, can be adapted to others requirements:
nc files in the correct projection (dimap files must already be reprojected),
written in 4D, even if the depth has only one entry. Time should be unlimited.
difference between _FillValue to indicate where no data_sh are available and missing_value to indicate land:
Change NaN to the usage of e.g. -999.999 for land and -888.888 for data_sh gaps
names written following the names convention

If any or all of the dimensions of a variable have the interpretations of ``date or time'' (T), ``height or depth'' (Z),
``latitude'' (Y), or ``longitude'' (X) then we recommend, but do not require (see section 1.4), those dimensions to
appear in the relative order T, then Z, then Y, then X in the CDL definition corresponding to the file. All other
dimensions should, whenever possible, be placed to the left of the spatiotemporal dimensions.
'''

import os
import numpy as np
import jdcal
import time
import snappy
from netCDF4 import Dataset
from demarine_output_prep.netcdf_methods import create_nc_vars, create_netcdf_dataset_dimensions_from_beam
from demarine_input_prep.demarine_paths import modisL3_TSMDemarine_CoarseGrid_Path, modisL3_nc_CoarseGrid_Path, modisL3_TSMDemarine_FineGrid_Path, modisL3_nc_FineGrid_Path

# input_variables = ['TSM_mean', 'CHL_mean', 'SST2_mean', 'KdPAR2_mean', 'PAR2_mean',
#                    'num_obs', 'num_passes', 'CHL_sigma', 'CHL_counts', 'TSM_sigma', 'TSM_counts',
#                    'SST2_sigma', 'SST2_counts', 'KdPAR2_sigma',
#                    'KdPAR2_counts', 'PAR2_sigma', 'PAR2_counts']
# output_variables = ['TSM', 'CHL', 'SST', 'KdPAR', 'PAR', 'num_obs', 'num_passes',
#                     'CHL_sigma', 'CHL_counts', 'TSM_sigma', 'TSM_counts', 'SST_sigma', 'SST_counts', 'KdPAR_sigma',
#                     'KdPAR_counts', 'PAR_sigma', 'PAR_counts']  # in the same order as input_variables
# output_variables_units = ['g/m^3', 'mg/m^3', 'degrees-C', 'dl', 'micromol/s^1/m^2',
#                           'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl', 'dl']
# output_variables_long_name = ['Total suspended matter concentration', 'Chlorophyll a concentration',
#                               'Sea Surface Temperature',
#                               'light attenuation coefficient at PAR', 'Photosynthetically Available Radiation',
#                               'number of observations', 'number of satellite overpass',
#                               'Chlorophyll standard deviation', 'number of Chlorophyll counts',
#                               'TSM standard deviation', 'number of TSM counts',
#                               'SST standard deviation', 'number of SST counts',
#                               'KdPAR standard deviation', 'number of KdPAR counts',
#                               'PAR standard deviation', 'number of PAR counts']
# output_variables_standard_name = ['TSM', 'CHL', 'SST', 'KdPAR', 'PAR', 'num_obs', 'num_passes',
#                                   'CHL_sigma', 'CHL_counts', 'TSM_sigma', 'TSM_counts',
#                                   'SST_sigma', 'SST_counts', 'KdPAR_sigma',
#                                   'KdPAR_counts', 'PAR_sigma', 'PAR_counts']


input_variables = ['CHL_mean']
output_variables = ['chl']  # in the same order as input_variables
output_variables_units = ['mg/m^3']
output_variables_long_name = ['Chlorophyll a concentration']
output_variables_standard_name = ['chl']

input_directory = modisL3_TSMDemarine_CoarseGrid_Path
output_directory = modisL3_nc_CoarseGrid_Path


# input_file = [f for f in sorted(os.listdir(input_directory)) if
#                os.path.isfile(os.path.join(input_directory, f)) and os.path.basename(f).endswith('.dim')]
input_files = ['reprojected_DeMarine_20150521_coarse_grid.dim',
 'reprojected_DeMarine_20150522_coarse_grid.dim',
 'reprojected_DeMarine_20150523_coarse_grid.dim',
 'reprojected_DeMarine_20150524_coarse_grid.dim',
 'reprojected_DeMarine_20150525_coarse_grid.dim']  # ,
#  'reprojected_DeMarine_20150512_coarse_grid.dim',
#  'reprojected_DeMarine_20150513_coarse_grid.dim',
#  'reprojected_DeMarine_20150514_coarse_grid.dim',
#  'reprojected_DeMarine_20150515_coarse_grid.dim',
#  'reprojected_DeMarine_20150516_coarse_grid.dim',
#  'reprojected_DeMarine_20150517_coarse_grid.dim',
#  'reprojected_DeMarine_20150518_coarse_grid.dim',]

# to get the lats and lons

ori_file = '/data/carole/DeMarine_dineof/input_files/DeMarine_coarse_2008_chl_HIGLINT_noPRODWARN_noHISOLZEN_input.nc'
original_file = Dataset(ori_file, mode='r')
lat_ori = original_file.variables['latitude']
lon_ori = original_file.variables['longitude']

some_product = snappy.ProductIO.readProduct(os.path.join(input_directory, input_files[0]))
width = some_product.getSceneRasterWidth()
height = some_product.getSceneRasterHeight()

watermask_product = snappy.ProductIO.readProduct(snappy.File('/data/carole/DeMarine_dineof_nrt/watermasks/watermask_DeMarine_coarse.dim'), ['BEAM-DIMAP'])

watermask_band = watermask_product.getBand('land_water_fraction')
watermask = np.zeros(width, dtype=np.float32)

base_jd = jdcal.gcal2jd(1970, 1, 1)[1]

for input_file in input_files:
    # t1 = time.perf_counter()
    output_file = os.path.join(output_directory, os.path.splitext(input_file)[0] + '.nc')

    dataset, lon_variable, lat_variable, time_variable, depth_variable = create_netcdf_dataset_dimensions_from_beam(
        some_product, output_file)
    # MODISA_L3_DeM_20081231_reproject_fine_grid
    # current_date = int(jdcal.gcal2jd(int(input_file[21:25]), int(input_file[25:27]), int(input_file[27:29]))[1])
    # current_date = int(jdcal.gcal2jd(int(input_file[3:7]), int(input_file[8:10]), int(input_file[11:13]))[1])
    current_date = int(jdcal.gcal2jd(int(input_file[21:25]),int(input_file[25:27]),int(input_file[27:29]))[1])
    # reprojected_DeMarine_20081231_fine_grid.data
    # L3_2008-05-08_2008-05-08
    time_variable[0] = current_date - base_jd
    depth_variable[0] = 0.0
    lat_variable[:] = lat_ori[:]
    lon_variable[:] = lon_ori[:]
    print('Reading product \'' + input_file + '\'')
    file = snappy.File(os.path.join(input_directory, input_file))
    current_product = snappy.ProductIO.readProduct(file,['BEAM-DIMAP'])



    create_nc_vars(dataset, input_variables, output_variables, output_variables_units,output_variables_long_name, output_variables_standard_name)
    # t3 =  time.perf_counter()
    # delta311sum = 0.0
    # delta312sum = 0.0
    for index, var in enumerate(input_variables):
        # t30 = time.perf_counter()
        data = np.zeros(width, dtype=np.float32)
        data[:] = 9999.0
        current_band = current_product.getBand(var)
        target_variable = dataset.variables[output_variables[index]]
        # t31 = time.perf_counter()
        # delta31 = t31 - t30
        # print("check-1 = {:0.6f} micro_seconds".format(delta31 * 1000000))
        for y in range(height):
            # t310 = time.perf_counter()
            current_band.readPixels(0, y, width, 1, data)
            # t311 = time.perf_counter()
            # delta311 = t311 - t310
            # print("delta310 = {:0.6f} micro_seconds".format(delta311 * 1000000))
            # delta311sum += delta311

            watermask_band.readPixels(0, y, width, 1, watermask)
            data = np.where(watermask == 0.0, 9999.0, data)
            data = data.reshape((1, 1, 1, width))
            # t311 = time.perf_counter()
            target_variable[:, :, y: y + 1, 0: width] = data
            # t312 = time.perf_counter()
            # delta312 = t312 - t311
            # print("delta311 = {:0.6f} micro_seconds".format(delta312 * 1000000))
            # delta312sum += delta312
        # t32 = time.perf_counter()
        # delta32 = t32 - t31
        # print("check-2 = {:0.6f} micro_seconds".format(delta32 * 1000000))



    # t4 = time.perf_counter()
    # delta1 = t2 - t1
    # delta2 = t3 - t2
    # delta3 = t4 - t3
    # delta_counts = len(input_variables)*height
    # mean_delta310 = delta311sum / delta_counts
    # mean_delta311 = delta312sum / delta_counts
    current_product.dispose()
    dataset.close()

    # print("t2 - t1 = {:0.6f} micro_seconds".format(delta1 * 1000000))
    # print("t3 - t2 = {:0.6f} micro_seconds".format(delta2 * 1000000))
    # print("t4 - t3 = {:0.6f} micro_seconds".format(delta3 * 1000000))
    # print("mean_delta310 = {:0.6f} micro_seconds".format(mean_delta310 * 1000000))
    # print("mean_delta311 = {:0.6f} micro_seconds".format(mean_delta311 * 1000000))


some_product.dispose()