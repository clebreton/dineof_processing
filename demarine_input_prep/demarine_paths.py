__author__ = 'carole'


# !!! file and paths are to work on bcserver13 directly !!

modisBaseInputPath = '/data/carole/INPUT_data/'          # bcserver 13

modisBaseOutputPath = 'W:/DeMarine/'         # bcserver 12-data_sh

modisL2_TSMBasePath_ns = 'S:/MODISA/L2_TSM/STD/NorthSea/'
modisL2_TSMBasePath_bs = 'R:/MODISA/L2_TSM/STD/BalticSea/'
# modisL3_TSMBasePath  = modisBaseOutputPath + 'L3_BINNED/'

modisL3_TSMBasePath = '/data/carole/INPUT_data/'
modisL3_TSMDemarine_FineGrid_Path = modisL3_TSMBasePath + 'L3_REPROJECT_FINE/'
modisL3_TSMDemarine_CoarseGrid_Path = modisL3_TSMBasePath + 'L3_REPROJECT_COARSE/'

modisL3_nc_CoarseGrid_Path = modisL3_TSMDemarine_CoarseGrid_Path + 'nc/'
modisL3_nc_FineGrid_Path = modisL3_TSMDemarine_FineGrid_Path + 'nc/'

seadasHome = '/home/uwe/tools/seadas/6.4/'                  # bcserver7 (deployment)

seadasScriptsDir = seadasHome + 'run/scripts/'

seadasBinDir = seadasHome + 'run/bin/linux/'             # bcserver7 (deployment)

#imageMagickBinDir = '/usr/local/bin/'                      # bcmacpro1 (development)
imageMagickBinDir = '/usr/bin/'                          # bcserver7 (deployment)



