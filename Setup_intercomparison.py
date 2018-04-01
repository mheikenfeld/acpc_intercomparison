from collections import OrderedDict,defaultdict
f = lambda: defaultdict(f) 

from load_models.load_WRF import load_WRF
from load_models.load_RAMS import load_RAMS
from load_models.load_COSMO import load_COSMO
from load_models.load_UM import load_UM
#from load_models_PJM.load_UM import load_UM_hrly


# Loading Functions:
# Specify which load module to use for each model
load_variable_cube=OrderedDict()
load_variable_cube['WRF_OXF']=load_WRF
load_variable_cube['WRF_NASA']=load_WRF
load_variable_cube['WRF_HIJU']=load_WRF
load_variable_cube['RAMS_CSU']=load_RAMS
load_variable_cube['COSMO_KIT']=load_COSMO
load_variable_cube['UM_LEEDS']=load_UM

# Specify colors for the models
color=OrderedDict()
color['WRF_OXF']='#002147'
color['WRF_HIJU']='#77d8d8'
color['WRF_NASA']='#0B3D91'
color['RAMS_CSU']='#1E4D2B'
color['COSMO_KIT']='#009682'
color['UM_LEEDS']='#b31b1b'


# Specify Variable names in the different models
variable_names=OrderedDict()
variable_names['WRF_OXF']=OrderedDict()
variable_names['WRF_NASA']=OrderedDict()
variable_names['WRF_HIJU']=OrderedDict()
variable_names['RAMS_CSU']=OrderedDict()
variable_names['COSMO_KIT']=OrderedDict()
variable_names['UM_LEEDS']=OrderedDict()

# Specify variable name and unique variable id for each model
new_varname = 'AccumPrecip'
variable_names['WRF_OXF'][new_varname]='RAINNC'
variable_names['RAMS_CSU'][new_varname]='ACCPR'
variable_names['COSMO_KIT'][new_varname]='TOT_PREC'
variable_names['UM_LEEDS'][new_varname]='pcp_accum'
variable_names['WRF_NASA'][new_varname]='RAINNC'


# Specify variable name and unique variable id for each model
new_varname = 'OLR'
variable_names['WRF_OXF'][new_varname]='OLR'
variable_names['RAMS_CSU'][new_varname]='OLR'
variable_names['COSMO_KIT'][new_varname]='THBT_RAD'
variable_names['UM_LEEDS'][new_varname]='LWup_TOA'
variable_names['WRF_NASA'][new_varname]='OLR'


# Specify variable name and unique variable id for each model
new_varname = 'W'
variable_names['WRF_OXF'][new_varname]='W'
variable_names['RAMS_CSU'][new_varname]='WC'
variable_names['COSMO_KIT'][new_varname]='W'
variable_names['UM_LEEDS'][new_varname]='w'
variable_names['WRF_NASA'][new_varname]='W'


new_varnames = ('QCLD','QRAIN','QICE','QSNOW','QGRA','QDRI','QAGG','QHAIL')

new_varname = 'QCLD'
variable_names['WRF_OXF'][new_varname]='QCLOUD'
variable_names['RAMS_CSU'][new_varname]='RCP'
variable_names['COSMO_KIT'][new_varname]='QC'
variable_names['UM_LEEDS'][new_varname]='qc'
variable_names['WRF_NASA'][new_varname]='QCLOUD'

new_varname = 'QRAIN'
variable_names['WRF_OXF'][new_varname]='QRAIN'
variable_names['RAMS_CSU'][new_varname]='RRP'
variable_names['COSMO_KIT'][new_varname]='QR'
variable_names['UM_LEEDS'][new_varname]='qr'
variable_names['WRF_NASA'][new_varname]='QRAIN'


new_varname = 'QDRI' # Only RAMS has DRIZZLE
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RDP'
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''

new_varname = 'QICE'
variable_names['WRF_OXF'][new_varname]='QICE'
variable_names['RAMS_CSU'][new_varname]='RPP'
variable_names['COSMO_KIT'][new_varname]='QI'
variable_names['UM_LEEDS'][new_varname]='qi'
variable_names['WRF_NASA'][new_varname]='QICE'

new_varname = 'QSNOW'
variable_names['WRF_OXF'][new_varname]='QSNOW'
variable_names['RAMS_CSU'][new_varname]='RSP'
variable_names['COSMO_KIT'][new_varname]='QS'
variable_names['UM_LEEDS'][new_varname]='qs'
variable_names['WRF_NASA'][new_varname]='QSNOW'

new_varname = 'QAGG' # Only RAMS has aggregate category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RAP'
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''

new_varname = 'QGRA'  
variable_names['WRF_OXF'][new_varname]='QGRAUP'
variable_names['RAMS_CSU'][new_varname]='RGP'
variable_names['COSMO_KIT'][new_varname]='QG'
variable_names['UM_LEEDS'][new_varname]='qg'
#variable_names['WRF_NASA'][new_varname]='QGRAUP'

new_varname = 'QHAIL' # Only RAMS has Hail category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RHP'
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''



#%%
# Filenames and Directories
# Specify file names and file paths:
filename=defaultdict(f)

filename['4500m']=OrderedDict()
filename['4500m']['WRF_OXF']="wrfout_d01*"
filename['4500m']['RAMS_CSU']="a-A*-g1.h5"
filename['4500m']['COSMO_KIT']="lfff*0000.nc"
filename['4500m']['UM_LEEDS']="*201306*.nc"
filename['4500m']['WRF_NASA']="wrfout_d01*00:00"

filename['1500m']=OrderedDict()
filename['1500m']['WRF_OXF']="wrfout_d02*"
filename['1500m']['RAMS_CSU']="a-A*-g2.h5"
filename['1500m']['COSMO_KIT']="lfff*0000.nc"
filename['1500m']['UM_LEEDS']="*201306*.nc"
filename['1500m']['WRF_NASA']="wrfout_d02*00:00"

filename['500m']=OrderedDict()
filename['500m']['WRF_OXF']="wrfout_d03*"
filename['500m']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['COSMO_KIT']="lfff*0000.nc"
filename['500m']['UM_LEEDS']="*201306*.nc"
filename['500m']['WRF_NASA']="wrfout_d03*00:00"


directory=defaultdict(f)

directory['CLN']['500m']['1h']=OrderedDict()
directory['CLN']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/WRF_ACPC_201306191200_hourly_CLN/d03"
directory['CLN']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/x.hrly"
directory['CLN']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_1h"
directory['CLN']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_CLN/D03"

directory['POL']['500m']['1h']=OrderedDict()
directory['POL']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/WRF_ACPC_201306191200_hourly_POL/d03"
directory['POL']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/x.hrly"
directory['POL']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_1h"
directory['POL']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_POL/D03"

directory['CLN']['500m']['5m']=OrderedDict()
directory['CLN']['500m']['5m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/WRF_ACPC_201306191800_1h1h5min_CLN/d03"
directory['CLN']['500m']['5m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/x.out.5m"
directory['CLN']['500m']['5m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['5m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_5m"
directory['CLN']['500m']['5m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_CLN"

directory['POL']['500m']['5m']=OrderedDict()
directory['POL']['500m']['5m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/WRF_ACPC_201306191800_1h1h5min_POL/d03"
directory['POL']['500m']['5m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/x.out.5m"
directory['POL']['500m']['5m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['5m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_5m"
directory['POL']['500m']['5m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_POL"

directory['CLN']['500m']['1m']=OrderedDict()
directory['CLN']['500m']['1m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/WRF_ACPC_201306191800_1h1h1min_CLN/d03"
directory['CLN']['500m']['1m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/x.out.5m"
directory['CLN']['500m']['1m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['1m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_5m"
directory['CLN']['500m']['1m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_CLN"

directory['POL']['500m']['1m']=OrderedDict()
directory['POL']['500m']['1m']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/WRF_ACPC_201306191800_1h1h1min_POL/d03"
directory['POL']['500m']['1m']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/x.out.1m"
directory['POL']['500m']['1m']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['1m']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_1m"
directory['POL']['500m']['1m']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_POL"

######################################################    
...
