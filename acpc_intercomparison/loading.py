from collections import OrderedDict

from .load_models.load_WRF import load_WRF
from .load_models.load_RAMS import load_RAMS
from .load_models.load_COSMO import load_COSMO
from .load_models.load_UM import load_UM
from .load_models.load_MesoNH import load_MesoNH

from .info import model_list, case_list, dt_list, dx_list
from .files import directory,filename
from .variables import variable_names

import glob,os

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

def load(variable, model=None, case=None, dx=None, dt=None):
    '''
    function to load cube by supplying information about model, case, time and spatial resolution as well as the variable
    '''
    #Check input parameters for consistency
    if model not in model_list:
        raise ValueError(f'model {model} not supported must be in {model_list}')
    if case not in case_list:
        raise ValueError(f'case {case} not supported must be in {case_list}')
    if dx not in dx_list:
        raise ValueError(f'dx {dx} not supported must be in {dx_list}')
    if dt not in dt_list:
        raise ValueError(f'dt {dt} not supported must be in {dt_list}')
    if dt in ['5m','1m'] and dx !='500m':
        raise ValueError(f'dt {dt} only avaliable in inner domain at 500m resolution')
        
    files=glob.glob(os.path.join(directory[case][dx][dt][model],filename[dx][dt][model]))
    return load_variable_cube[model](files,variable_names[model][variable])
        