#!/usr/bin/env python3
__author__ = 'uwe'

inputBaseDir = "/data/carole/INPUT_data/L3_REPROJECT_COARSE/"

trigger_dir = inputBaseDir + "signals/"
trigger_file = trigger_dir + "dineof_trigger.txt"
trigger_lock = trigger_file.replace("txt", "lck")

productionBaseDir = '/data/carole/DeMarine_dineof_nrt/'
dineof_initDir = productionBaseDir + 'init_files/'
dineof_inputDir  = productionBaseDir + 'input_files/'
dineof_outputBaseDir = productionBaseDir + 'output_files/'

watermask_dir = productionBaseDir + 'watermasks/'
watermask_coarse_nc_file = watermask_dir + 'watermask_DeMarine_coarse.nc'
watermask_coarse_dim_file = watermask_dir + 'watermask_DeMarine_coarse.dim'
watermask_fine_nc_file = watermask_dir + 'watermask_DeMarine_fine.nc'
watermask_fine_dim_file = watermask_dir + 'watermask_DeMarine_fine.dim'

dineof_home = '/opt/dineof-3.0/'
dineof_executable = dineof_home + 'dineof'
