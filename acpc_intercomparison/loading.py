from collections import OrderedDict

from .load_models.load_WRF import load_WRF
from .load_models.load_RAMS import load_RAMS
from .load_models.load_COSMO import load_COSMO
from .load_models.load_UM import load_UM
from .load_models.load_MesoNH import load_MesoNH


# Loading Functions:
# Specify which load module to use for each model
load_variable_cube=OrderedDict()
load_variable_cube['WRF_OXF']=load_WRF
load_variable_cube['WRF_NASA']=load_WRF
load_variable_cube['RAMS_CSU']=load_RAMS
load_variable_cube['COSMO_KIT']=load_COSMO
load_variable_cube['UM_LEEDS']=load_UM
load_variable_cube['MesoNH_Toulouse']=load_MesoNH
load_variable_cube['WRF_PNNL']=load_WRF

