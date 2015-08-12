__author__ = 'carole'


from netCDF4 import Dataset
import numpy as np
import jdcal
from datetime import datetime, date
from os import path

# "C:\\Users\\carole\\temp\\miau.nc"
def create_netcdf_dataset_dimensions(width, height, output_file, add_depth=True):
    print(output_file)
    dataset = Dataset(output_file, mode='w', format='NETCDF4')  # NETCDF3_CLASSIC
    dataset.createDimension("longitude", width)
    dataset.createDimension("latitude", height)
    dataset.createDimension("time", None)
    lon_variable = dataset.createVariable('longitude', np.float64, ('longitude'))
    lon_variable.units = 'degree'
    lon_variable.long_name = 'longitude coordinate of projection'
    lon_variable.standard_name = 'longitude'
    lat_variable = dataset.createVariable('latitude', np.float64, ('latitude'))
    lat_variable.units = 'degree'
    lat_variable.long_name = 'latitude coordinate of projection'
    lat_variable.standard_name = 'latitude'
    time_variable = dataset.createVariable('time', np.float32, ('time'))
    time_variable.units = 'days since 1970-1-1 0:0:0'
    time_variable.long_name = 'time'
    if add_depth:
        dataset.createDimension("depth", None)
        depth_variable = dataset.createVariable('depth', np.float32, ('depth'))
        depth_variable.units = 'm'
        depth_variable.long_name = 'depth'
    else:
        depth_variable = None
    return dataset, lon_variable, lat_variable, time_variable, depth_variable


def create_netcdf_dataset_dimensions_from_beam(some_product, output_file):
    width = some_product.getSceneRasterWidth()
    height = some_product.getSceneRasterHeight()
    return create_netcdf_dataset_dimensions(width, height, output_file)


def create_nc_vars(dataset, input_variables, output_variables, output_variables_units, output_variables_long_name,
                   output_variables_standard_name):
    for index, var in enumerate(input_variables):
        data_type = np.float32
        variable = dataset.createVariable(output_variables[index], data_type,
                                          ('time', 'depth', 'latitude', 'longitude'), fill_value=9999.0, zlib=True,
                                          complevel=4, least_significant_digit=3)
        variable.units = output_variables_units[index]
        variable.long_name = output_variables_long_name[index]
        variable.standard_name = output_variables_standard_name[index]
        variable.missing_value = 9999.0


# input_variables = ['TSM_mean','CHL_mean','PIC2_mean','POC2_mean','SST2_mean','KdPAR2_mean','PAR2_mean',
#                    'num_obs','num_passes','CHL_sigma','CHL_counts', 'TSM_sigma','TSM_counts','PIC2_sigma',
#                    'PIC2_counts','POC2_sigma','POC2_counts','SST2_sigma','SST2_counts','KdPAR2_sigma',
#                    'KdPAR2_counts','PAR2_sigma','PAR2_counts'] #
# output_variables = ['TSM','CHL','PIC','POC','SST','KdPAR','PAR','num_obs','num_passes',
#                     'CHL_sigma','CHL_counts', 'TSM_sigma','TSM_counts','PIC_sigma',
#                     'PIC_counts','POC_sigma','POC_counts','SST_sigma','SST_counts','KdPAR_sigma',
#                     'KdPAR_counts','PAR_sigma','PAR_counts'] # in the same order as input_variables
# output_variables_units = ['g/m^3','mg/m^3','mol/m^3','mg/m^3','degrees-C','dl','micromol/s^1/m^2',
#                           'dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl','dl']
# output_variables_long_name = ['Total suspended matter concentration','Chlorophyll a concentration',
#                               'Calcite Concentration, Balch and Gordon',
#                               'Particulate Organic Carbon, D. Stramski, 2007 (443/555 version)','Sea Surface Temperature',
#                               'light attenuation coefficient at PAR','Photosynthetically Available Radiation',
#                               'number of observations','number of satellite overpass',
#                               'Chlorophyll standard deviation','number of Chlorophyll counts',
#                               'TSM standard deviation','number of TSM counts',
#                               'PIC standard deviation','number of PIC counts',
#                               'POC standard deviation','number POC counts',
#                               'SST standard deviation','number of SST counts',
#                               'KdPAR standard deviation','number of KdPAR counts',
#                               'PAR standard deviation','number of PAR counts']
# output_variables_standard_name = ['TSM','CHL','PIC','POC','SST','KdPAR','PAR','num_obs','num_passes',
#                     'CHL_sigma','CHL_counts', 'TSM_sigma','TSM_counts','PIC_sigma',
#                     'PIC_counts','POC_sigma','POC_counts','SST_sigma','SST_counts','KdPAR_sigma',
#                     'KdPAR_counts','PAR_sigma','PAR_counts']


def nc_time_slice(width, height, timeindex, t, base_jd, output_directory, input_filename, input_file, input_variable):
    date_georg = jdcal.jd2gcal(2400000.5, t + base_jd)
    year = int(date_georg[0])
    month = int(date_georg[1])
    day = int(date_georg[2])
    date = datetime(year, month, day)
    str_date = date.strftime('%Y-%m-%d')

    output_file = path.join(output_directory, path.splitext(input_filename)[0] + '_' + str_date + '.nc')

    dataset, lon_variable, lat_variable, time_variable, depth_variable = \
        create_netcdf_dataset_dimensions(width, height, output_file, add_depth=True)

    # input_variables = ['CHL_mean']
    # output_variables = ['CHL']
    # output_variables_units = ['mg/m^3']
    # output_variables_long_name = ['Chlorophyll a concentration']
    # output_variables_standard_name = ['CHL']
    input_variables = ['chl']
    output_variables = ['chl']
    output_variables_units = ['mg/m^3']
    output_variables_long_name = ['Chlorophyll a concentration']
    output_variables_standard_name = ['chl']
    create_nc_vars(dataset, input_variables, output_variables,
                   output_variables_units, output_variables_long_name, output_variables_standard_name)

    time_variable[0] = t
    lon_variable[:] = input_file.variables['longitude'][:]
    lat_variable[:] = input_file.variables['latitude'][:]

    depth_variable[0] = 0.0
    target_chl_variable = dataset.variables[output_variables[0]]
    input_data = input_variable[timeindex:timeindex + 1, :, :]
    data = input_data.reshape((1, 1, height, width))
    target_chl_variable[:, :, :, :] = data

    dataset.close()
