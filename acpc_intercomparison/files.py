import os

from collections import OrderedDict

#%%
# Filenames and Directories
# Specify file names and file paths:
filename=OrderedDict()
filename['4500m']=OrderedDict()
filename['4500m']['1h']=OrderedDict()
filename['4500m']['1h']['WRF_OXF']="wrfout_d01*"
filename['4500m']['1h']['RAMS_CSU']="a-A*-g1.h5"
filename['4500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['4500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['4500m']['1h']['WRF_NASA']="wrfout_d01*"
filename['4500m']['1h']['MesoNH_Toulouse']="4.5km201306*.nc"
filename['4500m']['1h']['WRF_PNNL']="wrfout_d01*"

filename['1500m']=OrderedDict()
filename['1500m']['1h']=OrderedDict()
filename['1500m']['1h']['WRF_OXF']="wrfout_d02*"
filename['1500m']['1h']['RAMS_CSU']="a-A*-g2.h5"
filename['1500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['1500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['1500m']['1h']['WRF_NASA']="wrfout_d02*"
filename['1500m']['1h']['MesoNH_Toulouse']="1.5km201306*.nc"
filename['1500m']['1h']['WRF_PNNL']="wrfout_d02*"

filename['500m']=OrderedDict()
filename['500m']['1h']=OrderedDict()
filename['500m']['1h']['WRF_OXF']="wrfout_d03*"
filename['500m']['1h']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['500m']['1h']['WRF_NASA']="wrfout_d03*"
filename['500m']['1h']['MesoNH_Toulouse']="500m201306*.nc"
filename['500m']['1h']['WRF_PNNL']="wrfout_d03*"

filename['500m']['5m']=OrderedDict()
filename['500m']['5m']['WRF_OXF']="wrfout_d03*"
filename['500m']['5m']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['5m']['COSMO_KIT']="lfff*00.nc_5min"
filename['500m']['5m']['UM_LEEDS']="*201306*.nc"
filename['500m']['5m']['WRF_NASA']="wrfout_d03*"
filename['500m']['5m']['MesoNH_Toulouse']="500m201306*.nc"
filename['500m']['5m']['WRF_PNNL']="wrfout_d03*"

filename['500m']['1m']=OrderedDict()
filename['500m']['1m']['WRF_OXF']="wrfout_d03*"
filename['500m']['1m']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['1m']['COSMO_KIT']="lfff*00.nc_1min"
filename['500m']['1m']['UM_LEEDS']="*201306*.nc"
filename['500m']['1m']['WRF_NASA']="wrfout_d03*"
filename['500m']['1m']['MesoNH_Toulouse']="500m201306*.nc"
filename['500m']['1m']['WRF_PNNL']="wrfout_d03*"

top_directory_1mode=OrderedDict()
top_directory_1mode['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode"
top_directory_1mode['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode"
top_directory_1mode['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode"
top_directory_1mode['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode"
top_directory_1mode['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode"
top_directory_1mode['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode"
top_directory_1mode['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode"


directory=OrderedDict()

directory['CLN']=OrderedDict()
directory['CLN']['4500m']=OrderedDict()
directory['CLN']['4500m']['1h']=OrderedDict()
directory['CLN']['4500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/CLN/1h/d01"
directory['CLN']['4500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/CLN/1h/g1"
directory['CLN']['4500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/CLN/4500m"
directory['CLN']['4500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/CLN/4p5km"
directory['CLN']['4500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/CLN/1h/d01"
directory['CLN']['4500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/CLN/1h/4500m/"
directory['CLN']['4500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/CLN/1h/d01"


directory['POL']=OrderedDict()
directory['POL']['4500m']=OrderedDict()
directory['POL']['4500m']['1h']=OrderedDict()
directory['POL']['4500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/POL/1h/d01"
directory['POL']['4500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/POL/1h/g1"
directory['POL']['4500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/POL/4500m"
directory['POL']['4500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/POL/4p5km"
directory['POL']['4500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/POL/1h/d01"
directory['POL']['4500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/POL/1h/4500m/"
directory['POL']['4500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/POL/1h/d01"

directory['CLN']['1500m']=OrderedDict()
directory['CLN']['1500m']['1h']=OrderedDict()
directory['CLN']['1500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/CLN/1h/d02"
directory['CLN']['1500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/CLN/1h/g2"
directory['CLN']['1500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/CLN/1500m"
directory['CLN']['1500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/CLN/1p5km"
directory['CLN']['1500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/CLN/1h/d02"
directory['CLN']['1500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/CLN/1h/1500m/"
directory['CLN']['1500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/CLN/1h/d02"

directory['POL']['1500m']=OrderedDict()
directory['POL']['1500m']['1h']=OrderedDict()
directory['POL']['1500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/POL/1h/d02"
directory['POL']['1500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/POL/1h/g2"
directory['POL']['1500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/POL/1500m"
directory['POL']['1500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/POL/1p5km"
directory['POL']['1500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/POL/1h/d02"
directory['POL']['1500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/POL/1h/1500m/"
directory['POL']['1500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/POL/1h/d02"

directory['CLN']['500m']=OrderedDict()
directory['CLN']['500m']['1h']=OrderedDict()
directory['CLN']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/CLN/1h/d03"
directory['CLN']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/CLN/1h/g3"
directory['CLN']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/CLN/500m"
directory['CLN']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/CLN/0p5km_1h"
directory['CLN']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/CLN/1h/d03"
directory['CLN']['500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/CLN/1h/500m/"
directory['CLN']['500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/CLN/1h/d03"

directory['POL']['500m']=OrderedDict()
directory['POL']['500m']['1h']=OrderedDict()
directory['POL']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/POL/1h/d03"
directory['POL']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/POL/1h/g3"
directory['POL']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/POL/500m"
directory['POL']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/POL/0p5km_1h"
directory['POL']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/POL/1h/d03"
directory['POL']['500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/POL/1h/500m/"
directory['POL']['500m']['1h']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/POL/1h/d03"

directory['CLN']['500m']['5m']=OrderedDict()
directory['CLN']['500m']['5m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/CLN/5min/d03"
directory['CLN']['500m']['5m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/CLN/5min/g3"
directory['CLN']['500m']['5m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/CLN/500m"
directory['CLN']['500m']['5m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/CLN/0p5km_5m"
directory['CLN']['500m']['5m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/CLN/5min/d03"
directory['CLN']['500m']['5m']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/CLN/5min/500m/"
directory['CLN']['500m']['5m']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/CLN/5min/d03"

directory['POL']['500m']['5m']=OrderedDict()
directory['POL']['500m']['5m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/POL/5min/d03"
directory['POL']['500m']['5m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/POL/5min/g3"
directory['POL']['500m']['5m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/POL/500m"
directory['POL']['500m']['5m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/POL/0p5km_5m"
directory['POL']['500m']['5m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/POL/5min/d03"
directory['POL']['500m']['5m']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/POL/5min/500m/"
directory['POL']['500m']['5m']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/POL/5min/d03"

directory['CLN']['500m']['1m']=OrderedDict()
directory['CLN']['500m']['1m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/CLN/1min/d03"
directory['CLN']['500m']['1m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/CLN/1min/g3"
directory['CLN']['500m']['1m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/CLN/500m"
directory['CLN']['500m']['1m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/CLN/0p5km_1m"
directory['CLN']['500m']['1m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/CLN/1min/d03"
directory['CLN']['500m']['1m']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/CLN/1min/500m/"
directory['CLN']['500m']['1m']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/CLN/1min/d03"

directory['POL']['500m']['1m']=OrderedDict()
directory['POL']['500m']['1m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/1mode/POL/1min/d03"
directory['POL']['500m']['1m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/1mode/POL/1min/g3"
directory['POL']['500m']['1m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/1mode/POL/500m"
directory['POL']['500m']['1m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/1mode/POL/0p5km_1m"
directory['POL']['500m']['1m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/1mode/POL/1min/d03"
directory['POL']['500m']['1m']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/1mode/POL/1min/500m/"
directory['POL']['500m']['1m']['WRF_PNNL']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_PNNL/1mode/POL/1min/d03"

######################################################    

