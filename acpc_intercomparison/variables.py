from collections import OrderedDict

# Specify Variable names in the different models
variable_names=OrderedDict()
variable_names['WRF_OXF']=OrderedDict()
variable_names['WRF_NASA']=OrderedDict()
variable_names['RAMS_CSU']=OrderedDict()
variable_names['COSMO_KIT']=OrderedDict()
variable_names['UM_LEEDS']=OrderedDict()
variable_names['MesoNH_Toulouse']=OrderedDict()
variable_names['WRF_PNNL']=OrderedDict()

# Specify variable name and unique variable id for each model
new_varname = 'AccumPrecip'
variable_names['WRF_OXF'][new_varname]='RAINNC'
variable_names['RAMS_CSU'][new_varname]='surface_precipitation_accumulated'
variable_names['COSMO_KIT'][new_varname]='TOT_PREC'
variable_names['UM_LEEDS'][new_varname]='AccumPrecip'
variable_names['WRF_NASA'][new_varname]='RAINNC' # should be surface_precipitation_accumulated
variable_names['MesoNH_Toulouse'][new_varname]='pcp_accum'
variable_names['WRF_PNNL'][new_varname]='RAINNC' # should be surface_precipitation_accumulated

# Specify variable name and unique variable id for each model
new_varname = 'OLR'
variable_names['WRF_OXF'][new_varname]='OLR'
variable_names['RAMS_CSU'][new_varname]='OLR'
variable_names['COSMO_KIT'][new_varname]='THBT_RAD'
variable_names['UM_LEEDS'][new_varname]='LWup_TOA'
variable_names['WRF_NASA'][new_varname]='TLWUP'
variable_names['MesoNH_Toulouse'][new_varname]='LWup_TOA'
variable_names['WRF_PNNL'][new_varname]='OLR'

# Specify variable name and unique variable id for each model
new_varname = 'W'
variable_names['WRF_OXF'][new_varname]='W'
variable_names['RAMS_CSU'][new_varname]='WC'
variable_names['COSMO_KIT'][new_varname]='W'
variable_names['UM_LEEDS'][new_varname]='w'
variable_names['WRF_NASA'][new_varname]='W'
variable_names['MesoNH_Toulouse'][new_varname]='w'
variable_names['WRF_PNNL'][new_varname]='W'

# Specify variable name and unique variable id for each model
new_varname = 'T'
variable_names['WRF_OXF'][new_varname]='air_temperature'
variable_names['RAMS_CSU'][new_varname]='air_temperature'
variable_names['COSMO_KIT'][new_varname]='T'
variable_names['UM_LEEDS'][new_varname]='T'
variable_names['WRF_NASA'][new_varname]='air_temperature'
variable_names['MesoNH_Toulouse'][new_varname]='T'
variable_names['WRF_PNNL'][new_varname]='air_temperature'

# Specify variable name and unique variable id for each model
new_varname = 'P'
variable_names['WRF_OXF'][new_varname]='air_pressure'
variable_names['RAMS_CSU'][new_varname]='air_pressure'
variable_names['COSMO_KIT'][new_varname]='P'
variable_names['UM_LEEDS'][new_varname]='P'
variable_names['WRF_NASA'][new_varname]='air_pressure'
variable_names['MesoNH_Toulouse'][new_varname]='P'
variable_names['WRF_PNNL'][new_varname]='air_pressure'

# Specify variable name and unique variable id for each model
new_varname = 'rho'
variable_names['WRF_OXF'][new_varname]='RHO'
variable_names['RAMS_CSU'][new_varname]='dn0'
#variable_names['COSMO_KIT'][new_varname]=''
variable_names['UM_LEEDS'][new_varname]='rho'
variable_names['WRF_NASA'][new_varname]='RHO'
variable_names['MesoNH_Toulouse'][new_varname]='rho'
variable_names['WRF_PNNL'][new_varname]='RHO'

# Specify variable name and unique variable id for each model
new_varname = 'U'
variable_names['WRF_OXF'][new_varname]='U'
variable_names['RAMS_CSU'][new_varname]='UC'
variable_names['COSMO_KIT'][new_varname]='U'
variable_names['UM_LEEDS'][new_varname]='u'
variable_names['WRF_NASA'][new_varname]='U'
variable_names['MesoNH_Toulouse'][new_varname]='U'
variable_names['WRF_PNNL'][new_varname]='U'

# Specify variable name and unique variable id for each model
new_varname = 'V'
variable_names['WRF_OXF'][new_varname]='V'
variable_names['RAMS_CSU'][new_varname]='VC'
variable_names['COSMO_KIT'][new_varname]='V'
variable_names['UM_LEEDS'][new_varname]='v'
variable_names['WRF_NASA'][new_varname]='V'
variable_names['MesoNH_Toulouse'][new_varname]='V'
variable_names['WRF_PNNL'][new_varname]='V'

new_varnames = ('QV','QCLD','QRAIN','QICE','QSNOW','QGRA','QDRI','QAGG','QHAIL','NCLD','NRAIN','NICE','NSNOW','NGRA','NDRI','NAGG','NHAIL','NAERO')

# Specify variable name and unique variable id for each model PJM Added
new_varname = 'QV' # kg / kg
variable_names['WRF_OXF'][new_varname]='QVAPOR'
variable_names['RAMS_CSU'][new_varname]='RV'
variable_names['COSMO_KIT'][new_varname]='QV'
variable_names['UM_LEEDS'][new_varname]='qv'
variable_names['WRF_NASA'][new_varname]='QVAPOR'
variable_names['MesoNH_Toulouse'][new_varname]='qv'
variable_names['WRF_PNNL'][new_varname]='QVAPOR'

new_varname = 'QCLD'
variable_names['WRF_OXF'][new_varname]='QCLOUD'
variable_names['RAMS_CSU'][new_varname]='RCP'
variable_names['COSMO_KIT'][new_varname]='QC'
variable_names['UM_LEEDS'][new_varname]='qc'
variable_names['WRF_NASA'][new_varname]='QCLOUD'
variable_names['MesoNH_Toulouse'][new_varname]='qc'
variable_names['WRF_PNNL'][new_varname]='QCLOUD'

new_varname = 'QRAIN'
variable_names['WRF_OXF'][new_varname]='QRAIN'
variable_names['RAMS_CSU'][new_varname]='RRP'
variable_names['COSMO_KIT'][new_varname]='QR'
variable_names['UM_LEEDS'][new_varname]='qr'
variable_names['WRF_NASA'][new_varname]='QRAIN'
variable_names['MesoNH_Toulouse'][new_varname]='qr'
variable_names['WRF_PNNL'][new_varname]='QRAIN'

new_varname = 'QDRI' # Only RAMS has DRIZZLE
variable_names['RAMS_CSU'][new_varname]='RDP'

new_varname = 'QAGG' # Only RAMS has aggregate category
variable_names['RAMS_CSU'][new_varname]='RAP'

new_varname = 'QICE'
variable_names['WRF_OXF'][new_varname]='QICE'
variable_names['RAMS_CSU'][new_varname]='RPP'
variable_names['COSMO_KIT'][new_varname]='QI'
variable_names['UM_LEEDS'][new_varname]='qi'
variable_names['WRF_NASA'][new_varname]='QICE'
variable_names['MesoNH_Toulouse'][new_varname]='qi'
variable_names['WRF_PNNL'][new_varname]='QICE'

new_varname = 'QSNOW'
variable_names['WRF_OXF'][new_varname]='QSNOW'
variable_names['RAMS_CSU'][new_varname]='RSP'
variable_names['COSMO_KIT'][new_varname]='QS'
variable_names['UM_LEEDS'][new_varname]='qs'
variable_names['WRF_NASA'][new_varname]='QSNOW'
variable_names['MesoNH_Toulouse'][new_varname]='qs'
variable_names['WRF_PNNL'][new_varname]='QSNOW'

new_varname = 'QGRA'  
variable_names['WRF_OXF'][new_varname]='QGRAUP'
variable_names['RAMS_CSU'][new_varname]='RGP'
variable_names['COSMO_KIT'][new_varname]='QG'
variable_names['UM_LEEDS'][new_varname]='qg'
variable_names['WRF_NASA'][new_varname]='QGRAUP'
variable_names['MesoNH_Toulouse'][new_varname]='qg'
variable_names['WRF_PNNL'][new_varname]='QGRAUP'

new_varname = 'QHAIL' # Only RAMS has Hail category
variable_names['RAMS_CSU'][new_varname]='RHP'
variable_names['COSMO_KIT'][new_varname]='QH'

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
variable_names['WRF_PNNL'][new_varname]='QNRAIN'

new_varname = 'NDRI' # Only RAMS has DRIZZLE
variable_names['RAMS_CSU'][new_varname]='CDP' # #/kg

new_varname = 'NAGG' # Only RAMS has aggregate category
variable_names['RAMS_CSU'][new_varname]='CAP' # #/kg

new_varname = 'NICE'
variable_names['WRF_OXF'][new_varname]='QNICE' # #/kg
variable_names['RAMS_CSU'][new_varname]='CPP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCICE' # #/kg
variable_names['UM_LEEDS'][new_varname]='ni' # #/kg
variable_names['WRF_NASA'][new_varname]='QNICE'
variable_names['MesoNH_Toulouse'][new_varname]='ni' # #/kg
variable_names['WRF_PNNL'][new_varname]='QNICE' # #/kg

new_varname = 'NSNOW' 
variable_names['WRF_OXF'][new_varname]='QNSNOW' # #/kg
variable_names['RAMS_CSU'][new_varname]='CSP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCSNOW' # #/kg
variable_names['UM_LEEDS'][new_varname]='ns' # #/kg
variable_names['WRF_NASA'][new_varname]='QNSNOW' # #/kg
variable_names['MesoNH_Toulouse'][new_varname]='ns' # #/kg
variable_names['WRF_PNNL'][new_varname]='QNSNOW' # #/kg

new_varname = 'NGRA'
variable_names['WRF_OXF'][new_varname]='QNGRAUPEL' # #/kg
variable_names['RAMS_CSU'][new_varname]='CGP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCGRAUPEL' # #/kg
variable_names['UM_LEEDS'][new_varname]='ng' # #/kg
variable_names['WRF_NASA'][new_varname]='QNGRAUPEL'
variable_names['MesoNH_Toulouse'][new_varname]='ng' # #/kg
variable_names['WRF_PNNL'][new_varname]='QNGRAUPEL'

new_varname = 'NHAIL' # Only RAMS and COSMO has Hail category
variable_names['RAMS_CSU'][new_varname]='CHP' # #/kg
variable_names['COSMO_KIT'][new_varname]='NCHAIL' # #/kg

new_varname = 'NAERO' # 
variable_names['RAMS_CSU'][new_varname]='CCCNP' # #/kg
variable_names['UM_LEEDS'][new_varname]='na' # #/kg
variable_names['MesoNH_Toulouse'][new_varname]='n_ccn_free'
#variable_names['COSMO_KIT'][new_varname]='...'
variable_names['WRF_OXF'][new_varname]='NAER1' # #/kg
variable_names['WRF_NASA'][new_varname]='NA1' # #/kg
variable_names['WRF_PNNL'][new_varname]='QNCCN' # #/kg

#Hydrometeors as CubeLists:
new_varname = 'liquid_hydrometeors' # kg / kg
variable_names['WRF_OXF'][new_varname]=['QCLOUD','QRAIN']
variable_names['RAMS_CSU'][new_varname]=['RCP','RRP','RDP']
variable_names['COSMO_KIT'][new_varname]=['QC','QR']
variable_names['UM_LEEDS'][new_varname]=['qc','qr']
variable_names['WRF_NASA'][new_varname]=['QCLOUD','QRAIN']
variable_names['MesoNH_Toulouse'][new_varname]=['qc','qr']
variable_names['WRF_PNNL'][new_varname]=['QCLOUD','QRAIN']

new_varname = 'ice_hydrometeors' # kg / kg
variable_names['WRF_OXF'][new_varname]=['QICE','QSNOW','QGRAUP']
variable_names['RAMS_CSU'][new_varname]=['RPP','RSP','RAP','RGP','RHP']
variable_names['COSMO_KIT'][new_varname]=['QI','QS','QG','QH']
variable_names['UM_LEEDS'][new_varname]=['qi','qs','qg']
variable_names['WRF_NASA'][new_varname]=['QICE']
variable_names['MesoNH_Toulouse'][new_varname]=['qi','qs','qg']
variable_names['WRF_PNNL'][new_varname]=['QICE','QSNOW','QGRAUP']

new_varname = 'hydrometeors' # kg / kg
variable_names['WRF_OXF'][new_varname]=variable_names['WRF_OXF']['liquid_hydrometeors']+variable_names['WRF_OXF']['ice_hydrometeors']
variable_names['RAMS_CSU'][new_varname]=variable_names['RAMS_CSU']['liquid_hydrometeors']+variable_names['RAMS_CSU']['ice_hydrometeors']
variable_names['COSMO_KIT'][new_varname]=variable_names['COSMO_KIT']['liquid_hydrometeors']+variable_names['COSMO_KIT']['ice_hydrometeors']
variable_names['UM_LEEDS'][new_varname]=variable_names['UM_LEEDS']['liquid_hydrometeors']+variable_names['UM_LEEDS']['ice_hydrometeors']
variable_names['WRF_NASA'][new_varname]=variable_names['WRF_NASA']['liquid_hydrometeors']+variable_names['WRF_NASA']['ice_hydrometeors']
variable_names['MesoNH_Toulouse'][new_varname]=variable_names['MesoNH_Toulouse']['liquid_hydrometeors']+variable_names['MesoNH_Toulouse']['ice_hydrometeors']
variable_names['WRF_PNNL'][new_varname]=variable_names['WRF_PNNL']['liquid_hydrometeors']+variable_names['WRF_PNNL']['ice_hydrometeors']

print(variable_names)
