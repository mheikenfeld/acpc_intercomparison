from collections import OrderedDict,defaultdict
f = lambda: defaultdict(f) 

from load_models.load_WRF import load_WRF
from load_models.load_RAMS import load_RAMS
from load_models.load_COSMO import load_COSMO
from load_models.load_UM import load_UM
from load_models.load_MesoNH import load_MesoNH


# Loading Functions:
# Specify which load module to use for each model
load_variable_cube=OrderedDict()
load_variable_cube['WRF_OXF']=load_WRF
load_variable_cube['WRF_NASA']=load_WRF
load_variable_cube['WRF_HIJU']=load_WRF
load_variable_cube['RAMS_CSU']=load_RAMS
load_variable_cube['COSMO_KIT']=load_COSMO
load_variable_cube['UM_LEEDS']=load_UM
load_variable_cube['MesoNH_Toulouse']=load_MesoNH

# Specify colors for the models
color=OrderedDict()
color['WRF_OXF']='darkblue'
color['WRF_HIJU']='#77d8d8'
color['WRF_NASA']='darkcyan'
color['RAMS_CSU']='darkgreen'
color['COSMO_KIT']='darkorange'
color['UM_LEEDS']='darkred'
color['MesoNH_Toulouse']='#9400D3'

# Specify Variable names in the different models
variable_names=OrderedDict()
variable_names['WRF_OXF']=OrderedDict()
variable_names['WRF_NASA']=OrderedDict()
variable_names['WRF_HIJU']=OrderedDict()
variable_names['RAMS_CSU']=OrderedDict()
variable_names['COSMO_KIT']=OrderedDict()
variable_names['UM_LEEDS']=OrderedDict()
variable_names['MesoNH_Toulouse']=OrderedDict()

# Specify variable name and unique variable id for each model
new_varname = 'AccumPrecip'
variable_names['WRF_OXF'][new_varname]='surface_precipitation_accumulated'
variable_names['RAMS_CSU'][new_varname]='surface_precipitation_accumulated'
variable_names['COSMO_KIT'][new_varname]='TOT_PREC'
variable_names['UM_LEEDS'][new_varname]='pcp_accum'
variable_names['WRF_NASA'][new_varname]='RAINNC'
variable_names['MesoNH_Toulouse'][new_varname]='pcp_accum'

# Specify variable name and unique variable id for each model
new_varname = 'OLR'
variable_names['WRF_OXF'][new_varname]='OLR'
variable_names['RAMS_CSU'][new_varname]='OLR'
variable_names['COSMO_KIT'][new_varname]='THBT_RAD'
variable_names['UM_LEEDS'][new_varname]='LWup_TOA'
variable_names['WRF_NASA'][new_varname]='TLWUP'
variable_names['MesoNH_Toulouse'][new_varname]='LWup_TOA'

# Specify variable name and unique variable id for each model
new_varname = 'W'
variable_names['WRF_OXF'][new_varname]='W'
variable_names['RAMS_CSU'][new_varname]='WC'
variable_names['COSMO_KIT'][new_varname]='W'
variable_names['UM_LEEDS'][new_varname]='w'
variable_names['WRF_NASA'][new_varname]='W'
variable_names['MesoNH_Toulouse'][new_varname]='w'

# Specify variable name and unique variable id for each model
new_varname = 'T'
variable_names['WRF_OXF'][new_varname]='air_temperature'
variable_names['RAMS_CSU'][new_varname]='air_temperature'
variable_names['COSMO_KIT'][new_varname]='T'
variable_names['UM_LEEDS'][new_varname]='T'
variable_names['WRF_NASA'][new_varname]='air_temperature'
variable_names['MesoNH_Toulouse'][new_varname]='T'

new_varnames = ('QV','QCLD','QRAIN','QICE','QSNOW','QGRA','QDRI','QAGG','QHAIL','NCLD','NRAIN','NICE','NSNOW','NGRA','NDRI','NAGG','NHAIL','NAERO')

# Specify variable name and unique variable id for each model PJM Added
new_varname = 'QV' # kg / kg
variable_names['WRF_OXF'][new_varname]='QVAPOR'
variable_names['RAMS_CSU'][new_varname]='RV'
variable_names['COSMO_KIT'][new_varname]='QV'
variable_names['UM_LEEDS'][new_varname]='qv'
variable_names['WRF_NASA'][new_varname]='QVAPOR'
variable_names['MesoNH_Toulouse'][new_varname]='qv'

new_varname = 'QCLD'
variable_names['WRF_OXF'][new_varname]='QCLOUD'
variable_names['RAMS_CSU'][new_varname]='RCP'
variable_names['COSMO_KIT'][new_varname]='QC'
variable_names['UM_LEEDS'][new_varname]='qc'
variable_names['WRF_NASA'][new_varname]='QCLOUD'
variable_names['MesoNH_Toulouse'][new_varname]='qc'

new_varname = 'QRAIN'
variable_names['WRF_OXF'][new_varname]='QRAIN'
variable_names['RAMS_CSU'][new_varname]='RRP'
variable_names['COSMO_KIT'][new_varname]='QR'
variable_names['UM_LEEDS'][new_varname]='qr'
variable_names['WRF_NASA'][new_varname]='QRAIN'
variable_names['MesoNH_Toulouse'][new_varname]='qr'

new_varname = 'QDRI' # Only RAMS has DRIZZLE
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RDP'
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=' '

new_varname = 'QICE'
variable_names['WRF_OXF'][new_varname]='QICE'
variable_names['RAMS_CSU'][new_varname]='RPP'
variable_names['COSMO_KIT'][new_varname]='QI'
variable_names['UM_LEEDS'][new_varname]='qi'
variable_names['WRF_NASA'][new_varname]='QICE'
variable_names['MesoNH_Toulouse'][new_varname]='qi'

new_varname = 'QSNOW'
variable_names['WRF_OXF'][new_varname]='QSNOW'
variable_names['RAMS_CSU'][new_varname]='RSP'
variable_names['COSMO_KIT'][new_varname]='QS'
variable_names['UM_LEEDS'][new_varname]='qs'
variable_names['WRF_NASA'][new_varname]='QSNOW'
variable_names['MesoNH_Toulouse'][new_varname]='qs'

new_varname = 'QAGG' # Only RAMS has aggregate category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RAP'
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=' '

new_varname = 'QGRA'  
variable_names['WRF_OXF'][new_varname]='QGRAUP'
variable_names['RAMS_CSU'][new_varname]='RGP'
variable_names['COSMO_KIT'][new_varname]='QG'
variable_names['UM_LEEDS'][new_varname]='qg'
#variable_names['WRF_NASA'][new_varname]='QGRAUP'
variable_names['MesoNH_Toulouse'][new_varname]='qg'

new_varname = 'QHAIL' # Only RAMS has Hail category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='RHP'
variable_names['COSMO_KIT'][new_varname]='QH'
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=''

new_varname = 'NCLD'
variable_names['WRF_OXF'][new_varname]='QNCLOUD'
variable_names['RAMS_CSU'][new_varname]='CCP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCCLOUD' # #/kg
variable_names['UM_LEEDS'][new_varname]='nc' # #/kg
variable_names['WRF_NASA'][new_varname]='QNCLOUD'
variable_names['MesoNH_Toulouse'][new_varname]='nc' # #/kg

new_varname = 'NRAIN'
variable_names['WRF_OXF'][new_varname]='QNRAIN'
variable_names['RAMS_CSU'][new_varname]='CRP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCRAIN' # #/kg
variable_names['UM_LEEDS'][new_varname]='nr' # #/kg
variable_names['WRF_NASA'][new_varname]='QNRAIN'
variable_names['MesoNH_Toulouse'][new_varname]='nr' # #/kg

new_varname = 'NDRI' # Only RAMS has DRIZZLE
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='CDP' # #/kg
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=' '

new_varname = 'NICE'
variable_names['WRF_OXF'][new_varname]='QNICE' # #/kg
variable_names['RAMS_CSU'][new_varname]='CPP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCICE' # #/kg
variable_names['UM_LEEDS'][new_varname]='ni' # #/kg
variable_names['WRF_NASA'][new_varname]='QNICE'
variable_names['MesoNH_Toulouse'][new_varname]='ni' # #/kg

new_varname = 'NSNOW' 
variable_names['WRF_OXF'][new_varname]='QNSNOW' # #/kg
variable_names['RAMS_CSU'][new_varname]='CSP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCSNOW' # #/kg
variable_names['UM_LEEDS'][new_varname]='ns' # #/kg
variable_names['WRF_NASA'][new_varname]='QNSNOW' # #/kg
variable_names['MesoNH_Toulouse'][new_varname]='ns' # #/kg

new_varname = 'NAGG' # Only RAMS has aggregate category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='CAP' # #/kg
#variable_names['COSMO_KIT'][new_varname]=''
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=' '

new_varname = 'NGRA'
variable_names['WRF_OXF'][new_varname]='QNGRAUPEL' # #/kg
variable_names['RAMS_CSU'][new_varname]='CGP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCGRAUPEL' # #/kg
variable_names['UM_LEEDS'][new_varname]='ng' # #/kg
variable_names['WRF_NASA'][new_varname]='QNGRAUPEL'
variable_names['MesoNH_Toulouse'][new_varname]='ng' # #/kg

new_varname = 'NHAIL' # Only RAMS and COSMO has Hail category
#variable_names['WRF_OXF'][new_varname]=''
variable_names['RAMS_CSU'][new_varname]='CHP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCHAIL' # #/kg
#variable_names['UM_LEEDS'][new_varname]=''
#variable_names['WRF_NASA'][new_varname]=''
#variable_names['MesoNH_Toulouse'][new_varname]=''

new_varname = 'NAERO' # 
# variable_names['WRF_OXF'][new_varname]='NAER1'
variable_names['RAMS_CSU'][new_varname]='CCCNP' # #/kg
# variable_names['COSMO_KIT'][new_varname]='' 
variable_names['UM_LEEDS'][new_varname]='na' # #/kg
# variable_names['WRF_NASA'][new_varname]=''
variable_names['MesoNH_Toulouse'][new_varname]='n_ccn_free'

#%%
# Filenames and Directories
# Specify file names and file paths:
filename=defaultdict(f)

filename['4500m']['1h']=OrderedDict()
filename['4500m']['1h']['WRF_OXF']="wrfout_d01*"
filename['4500m']['1h']['RAMS_CSU']="a-A*-g1.h5"
filename['4500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['4500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['4500m']['1h']['WRF_NASA']="wrfout_d01*"
filename['4500m']['1h']['MesoNH_Toulouse']="4.5km201306*.nc"

filename['1500m']['1h']=OrderedDict()
filename['1500m']['1h']['WRF_OXF']="wrfout_d02*"
filename['1500m']['1h']['RAMS_CSU']="a-A*-g2.h5"
filename['1500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['1500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['1500m']['1h']['WRF_NASA']="wrfout_d02*"
filename['1500m']['1h']['MesoNH_Toulouse']="1.5km201306*.nc"

filename['500m']['1h']=OrderedDict()
filename['500m']['1h']['WRF_OXF']="wrfout_d03*"
filename['500m']['1h']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['1h']['COSMO_KIT']="lfff*0000.nc"
filename['500m']['1h']['UM_LEEDS']="*201306*.nc"
filename['500m']['1h']['WRF_NASA']="wrfout_d03*"
filename['500m']['1h']['MesoNH_Toulouse']="500m201306*.nc"

filename['500m']['5min']=OrderedDict()
filename['500m']['5min']['WRF_OXF']="wrfout_d03*"
filename['500m']['5min']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['5min']['COSMO_KIT']="lfff*0000.nc_5min"
filename['500m']['5min']['UM_LEEDS']="*201306*.nc"
filename['500m']['5min']['WRF_NASA']="wrfout_d03*"
filename['500m']['5min']['MesoNH_Toulouse']="500m201306*.nc"

filename['500m']['1min']=OrderedDict()
filename['500m']['1min']['WRF_OXF']="wrfout_d03*"
filename['500m']['1min']['RAMS_CSU']="a-A*-g3.h5"
filename['500m']['1min']['COSMO_KIT']="lfff*0000.nc_1min"
filename['500m']['1min']['UM_LEEDS']="*201306*.nc"
filename['500m']['1min']['WRF_NASA']="wrfout_d03*"
filename['500m']['1min']['MesoNH_Toulouse']="500m201306*.nc"

directory=defaultdict(f)

directory['CLN']['1500m']['1h']=OrderedDict()
directory['CLN']['1500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/1h/d02"
directory['CLN']['1500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/1h/d02"
#directory['CLN']['1500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['1500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m_3DTurb_type7"
directory['CLN']['1500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_1h"
directory['CLN']['1500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/CLN/1h/d03"
directory['CLN']['1500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/cln/1p5km/"

directory['POL']['1500m']['1h']=OrderedDict()
directory['POL']['1500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/1h/d02"
directory['POL']['1500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/1h/d02"
#directory['POL']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['1500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m_3DTurb_type7"
directory['POL']['1500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_1h"
directory['POL']['1500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/POL/1h/d03"
directory['POL']['1500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/pol/1p5km/"

directory['CLN']['500m']['1h']=OrderedDict()
directory['CLN']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/1h/d03"
directory['CLN']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/1h/d03"
#directory['CLN']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m_3DTurb_type7"
directory['CLN']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_1h"
directory['CLN']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/CLN/1h/d03"
directory['CLN']['500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/cln/0p5km/"

directory['POL']['500m']['1h']=OrderedDict()
directory['POL']['500m']['1h']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/1h/d03"
directory['POL']['500m']['1h']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/1h/d03"
#directory['POL']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['1h']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m_3DTurb_type7"
directory['POL']['500m']['1h']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_1h"
directory['POL']['500m']['1h']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/POL/1h/d03"
directory['POL']['500m']['1h']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/pol/0p5km/"

directory['CLN']['500m']['5min']=OrderedDict()
directory['CLN']['500m']['5min']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/5min/d03"
directory['CLN']['500m']['5min']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/5min/d03"
#directory['CLN']['500m']['5min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['5min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m_3DTurb_type7"
directory['CLN']['500m']['5min']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_5m"
directory['CLN']['500m']['5min']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/CLN/5min/d03"
directory['CLN']['500m']['5min']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/cln/0p5km/"

directory['POL']['500m']['5min']=OrderedDict()
directory['POL']['500m']['5min']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/5min/d03"
directory['POL']['500m']['5min']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/5min/d03"
#directory['POL']['500m']['5min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['5min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m_3DTurb_type7"
directory['POL']['500m']['5min']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_5m"
directory['POL']['500m']['5min']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/POL/5min/d03"
directory['POL']['500m']['5min']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/pol/0p5km/"

directory['CLN']['500m']['1min']=OrderedDict()
directory['CLN']['500m']['1min']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/1min/d03"
directory['CLN']['500m']['1min']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/1min/d03"
#directory['CLN']['500m']['1min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
directory['CLN']['500m']['1min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m_3DTurb_type7"
directory['CLN']['500m']['1min']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_5m"
directory['CLN']['500m']['1min']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/CLN/1min/d03"
directory['CLN']['500m']['1min']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/cln/0p5km/"

directory['POL']['500m']['1min']=OrderedDict()
directory['POL']['500m']['1min']['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/1min/d03"
directory['POL']['500m']['1min']['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/1min/d03"
#directory['POL']['500m']['1min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
directory['POL']['500m']['1min']['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m_3DTurb_type7"
directory['POL']['500m']['1min']['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_1m"
directory['POL']['500m']['1min']['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/POL/1min/d03"
directory['POL']['500m']['1min']['MesoNH_Toulouse']="/group_workspaces/jasmin2/acpc/houston_deep_convection/MesoNH_Toulouse/pol/0p5km/"

######################################################    
...
