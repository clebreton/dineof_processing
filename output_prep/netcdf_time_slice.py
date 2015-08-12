__author__ = 'carole'

from os import path
from netCDF4 import Dataset
import jdcal
from output_prep.netcdf_methods import nc_time_slice  # create_nc_vars, create_netcdf_dataset_dimensions


input_directory = out_file = '/data/carole/DeMarine_dineof_nrt/output_files/DINEOF_DeM_chl_20150520'
input_filename = 'retrans_DINEOF_DeM_coarse_chl_output_20150520.nc'
input_file = Dataset(path.join(input_directory, input_filename), mode='r')
output_directory = '/data/carole/DeMarine_dineof_nrt/output_files/DINEOF_DeM_chl_20150520/daylies'

width = len(input_file.dimensions['longitude'])
height = len(input_file.dimensions['latitude'])
time_len = len(input_file.dimensions['time'])

input_variable_name = 'chl'  ## ''chl
input_variable = input_file.variables[input_variable_name]

# time definition
timevar = input_file.variables['time']
input_time = timevar[:]
base_jd = jdcal.gcal2jd(1970, 1, 1)[1]


for timeindex in range(len(input_time)):
    t = int(input_time[timeindex])
    nc_time_slice(width, height, timeindex, t, base_jd, output_directory, input_filename, input_file, input_variable)

input_file.close()
