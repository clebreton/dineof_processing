__author__ = 'carole'


beam_501HomeDir = '/opt/beam-5.0/'

beamHomeDir = beam_501HomeDir
beamBinDir  = beamHomeDir + 'bin/'
gptProcessor = beamBinDir + 'gpt.sh'
pconvProcessor = beamBinDir + 'pconvert.sh'
l3binningDir = '/data/carole/l3binning/'
# beamProcessingConfDir ='/home/uwe/cronjobs/bc/eodata/beam_processing/conf/'
beamProcessingConfDir ='/data/carole/dineof_processing/demarine_input_prep/'

DeMarine_fine_grid_graph_file = beamProcessingConfDir + 'reproject_BSH_fine.xml'
DeMarine_coarse_grid_graph_file = beamProcessingConfDir + 'reproject_BSH_coarse.xml'

cobios_chl_palette = '/home/uwe/tools/pconvert/color_palettes/chl_cobios.cpd'

imageMagickComposite = '/usr/bin/composite'
landMaskFile = '/home/uwe/tools/pconvert/cb_ns_overlay.png'

# L3 grid coordinates for DeMarine grid
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