__author__ = 'carole'

# toolsDir = '/home/uwe/tools/'
# beam410HomeDir = toolsDir + 'beam-4.10/'
beam_501HomeDir = 'C:/progra~1/beam-5.0/'

beamHomeDir = beam_501HomeDir
beamBinDir  = beamHomeDir + 'bin/'
gptProcessor = beamBinDir + 'gpt.bat'
pconvProcessor = beamBinDir + 'pconvert.bat'
binningProcessor = beamBinDir + 'binning.bat'
l3binningDir = 'W:/DeMarine/l3binning/'
# beamProcessingConfDir ='/home/uwe/cronjobs/bc/eodata/beam_processing/conf/'
beamProcessingConfDir ='C:/Users/carole/PycharmProjects/geoinfopy/sandbox/carole/DeMarine/'

DeMarine_fine_grid_graph_file = beamProcessingConfDir + 'reproject_BSH_fine.xml'
DeMarine_coarse_grid_graph_file = beamProcessingConfDir + 'reproject_BSH_coarse.xml'

cobios_chl_palette = '/home/uwe/tools/pconvert/color_palettes/chl_cobios.cpd'

imageMagickComposite = '/usr/bin/composite'
landMaskFile = '/home/uwe/tools/pconvert/cb_ns_overlay.png'

# L3 processing parameters for DeMarine grid:
west_lon_large_l3  = -4.50
east_lon_large_l3  =  32.00
south_lat_large_l3 =  50.50
north_lat_large_l3 =  64.00
# L3 grid coordinates for new binner for DeMarine
west_lon = -15.00
east_lon = 31.00
south_lat = 47.00
north_lat = 64.00

#region = POLYGON((west_lon north_lat,east_lon north_lat,east_lon south_lat,west_lon south_lat,west_lon north_lat))
region = 'POLYGON((-15.00 66.00, 31.00 66.00, 31.00 47.00, -15.00 47.00, -15.00 66.00))'

supersampling = 3
num_rows = 7436
product_format = 'BEAM-DIMAP'
compositing_type = 'BINNING'
output_Binned_Data = 'false'
output_format = 'BEAM-DIMAP'

l3_grid_cell_size = 1.2