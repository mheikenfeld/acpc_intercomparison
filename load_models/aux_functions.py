#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:18:46 2018
@author: heikenfeldl
"""
import numpy as np
from Setup_intercomparison import variable_names,load_variable_cube

def load_Condensate(files,model):

    Hydrometeors = ('QCLD','QRAIN','QICE','QSNOW','QGRA','QDRI','QAGG','QHAIL')

    COND={}

    if model == 'RAMS_CSU':
        for i in np.arange(0,len(Hydrometeors),1):
        # if i > 4: # RAMS has 3 additional hydrometeor variables, so they are accounted for here
                  # Probably better moving forward to move DRI with RAIN, AGG with SNOW, and HAIL with GRAUP in load module moving forward
            COND[i]=load_variable_cube[model](files,variable_names[model][Hydrometeors[i]])
    elif model == 'WRF_NASA':
        for i in np.arange(0,3):                
            COND[i]=load_variable_cube[model](files,variable_names[model][Hydrometeors[i]])
    elif model in ['WRF_OXF','COSMO_KIT','UM_LEEDS']:
        for i in np.arange(0,5):
            COND[i]=load_variable_cube[model](files,variable_names[model][Hydrometeors[i]])
    
    if model == 'RAMS_CSU':
        TCL = COND[0]+COND[1]+COND[5]
        TCI = COND[2]+COND[3]+COND[4]+COND[6]+COND[7]
        
    if model == 'WRF_NASA':
        TCL = COND[0]+COND[1]
        TCI = COND[2]
        
    elif model in ['WRF_OXF','COSMO_KIT','UM_LEEDS']:
        TCL = COND[0]+COND[1]
        TCI = COND[2]+COND[3]+COND[4]
        
    TC = TCI+TCL
    return TC,TCL,TCI
    # return TC


