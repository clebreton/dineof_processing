#!/usr/bin/env python3
__author__ = 'uwe'

baseDir = "/data/carole/INPUT_data/"
inputBaseDir = baseDir + "L3_subsets/"
trigger_dir = baseDir + "signals/"

productionBaseDir = '/data/carole/DeMarine_dineof_nrt/'
dineof_initDir = productionBaseDir + 'init_files/'
dineof_inputDir  = productionBaseDir + 'input_files/'
intermediate_Dir = baseDir + "L3_subsets"
dineof_outputBaseDir = productionBaseDir + 'output_files/'

watermask_dir = productionBaseDir + 'watermasks/'
watermask_dim_file = watermask_dir + 'L3_subset_watermask.dim'
watermask_nc_file = watermask_dir + 'L3_subset_watermask.nc'
watermask_coarse_nc_file = watermask_dir + 'watermask_DeMarine_coarse.nc'
watermask_coarse_dim_file = watermask_dir + 'watermask_DeMarine_coarse.dim'
watermask_fine_nc_file = watermask_dir + 'watermask_DeMarine_fine.nc'
watermask_fine_dim_file = watermask_dir + 'watermask_DeMarine_fine.dim'

dineof_home = '/opt/dineof-3.0/'
dineof_executable = dineof_home + 'dineof'
