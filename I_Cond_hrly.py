#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:25:41 2018

@author: pmarin
"""
# Code for Intermodel Comparsion
# Started by M.H., editted by PJM (3/21/18)
import numpy as np
import glob
import os
# Import Python Libraries
import iris.plot as iplt
from iris.analysis import MEAN, MAX, SUM

import matplotlib
matplotlib.pyplot.switch_backend('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict, OrderedDict
f = lambda: defaultdict(f) 

import warnings
warnings.filterwarnings('ignore', category=UserWarning, append=True)
warnings.filterwarnings('ignore', category=RuntimeWarning, append=True)
warnings.filterwarnings('ignore', category=FutureWarning, append=True)


savename = 'G3_hrly_'


models=[]
models.append('WRF_OXF')
models.append('RAMS_CSU')
models.append('COSMO_KIT')
models.append('UM_LEEDS')
models.append('WRF_NASA')

# Get filename paths for all the data
files_CLN_500m_1h=OrderedDict(); files_POL_500m_1h=OrderedDict()
for model in models:
    # print(os.path.join(directory['CLN']['500m']['1h'][model],filename['500m']['1h'][model]))
    files_CLN_500m_1h[model]=glob.glob(os.path.join(directory['CLN']['500m']['1h'][model],filename['500m']['1h'][model]))
    # print(os.path.join(directory['POL']['500m']['1h'][model],filename['500m']['1h'][model]))
    files_POL_500m_1h[model]=glob.glob(os.path.join(directory['POL']['500m']['1h'][model],filename['500m']['1h'][model]))
    
#########################################################################    
############## Load CONDENSATE data for each model, using specified load module
#########################################################################   
COND_CLN=OrderedDict()
COND_POL=OrderedDict()

Hydrometeors = ('QCLD','QRAIN','QICE','QSNOW','QGRA','QDRI','QAGG','QHAIL')

for model in models:            
    
    
    if model == 'RAMS_CSU':
        for i in np.arange(0,len(Hydrometeors),1):
        # if i > 4: # RAMS has 3 additional hydrometeor variables, so they are accounted for here
                  # Probably better moving forward to move DRI with RAIN, AGG with SNOW, and HAIL with GRAUP in load module moving forward
                # print(model,files_CLN_500m_1h[model])
            COND_CLN[model,i]=load_variable_cube[model](files_CLN_500m_1h[model],variable_names[model][Hydrometeors[i]])
            # print(model,files_CLN_500m_1h[model])
            COND_POL[model,i]=load_variable_cube[model](files_POL_500m_1h[model],variable_names[model][Hydrometeors[i]])            
    elif model == 'WRF_NASA':
        for i in np.arange(0,3):
            COND_CLN[model,i]=load_variable_cube[model](files_CLN_500m_1h[model],variable_names[model][Hydrometeors[i]])
                # print(model,files_CLN_500m_1h[model])
            COND_POL[model,i]=load_variable_cube[model](files_POL_500m_1h[model],variable_names[model][Hydrometeors[i]])            
    elif model in ['WRF_OXF','COSMO_KIT','UM_LEEDS']:
        for i in np.arange(0,5):
            # print(model,files_CLN_500m_1h[model])
            COND_CLN[model,i]=load_variable_cube[model](files_CLN_500m_1h[model],variable_names[model][Hydrometeors[i]])
            # print(model,files_CLN_500m_1h[model])
            COND_POL[model,i]=load_variable_cube[model](files_POL_500m_1h[model],variable_names[model][Hydrometeors[i]])            
            
TC_CLN=OrderedDict(); TCI_CLN = OrderedDict(); TCL_CLN = OrderedDict();
TC_POL=OrderedDict(); TCI_POL = OrderedDict(); TCL_POL = OrderedDict();
for model in models:
    if model == 'RAMS_CSU':
        TCL_CLN[model] = COND_CLN[model,0]+COND_CLN[model,1]+COND_CLN[model,5]
        TCL_POL[model] = COND_POL[model,0]+COND_POL[model,1]+COND_POL[model,5]
        TCI_CLN[model] = COND_CLN[model,2]+COND_CLN[model,3]+COND_CLN[model,4]+COND_CLN[model,6]+COND_CLN[model,7]
        TCI_POL[model] = COND_POL[model,2]+COND_POL[model,3]+COND_POL[model,4]+COND_POL[model,6]+COND_POL[model,7]
    if model == 'WRF_NASA':
        TCL_CLN[model] = COND_CLN[model,0]+COND_CLN[model,1]
        TCL_POL[model] = COND_POL[model,0]+COND_POL[model,1]
        TCI_CLN[model] = COND_CLN[model,2]
        TCI_POL[model] = COND_POL[model,2]
    elif model in ['WRF_OXF','COSMO_KIT','UM_LEEDS']:
        TCL_CLN[model] = COND_CLN[model,0]+COND_CLN[model,1]
        TCL_POL[model] = COND_POL[model,0]+COND_POL[model,1]
        TCI_CLN[model] = COND_CLN[model,2]+COND_CLN[model,3]+COND_CLN[model,4]
        TCI_POL[model] = COND_POL[model,2]+COND_POL[model,3]+COND_POL[model,4]
        
    TC_CLN[model] = TCI_CLN[model]+TCL_CLN[model]
    TC_POL[model] = TCI_POL[model]+TCL_POL[model]       

#########################################################################
####### PLOTTING
#########################################################################

############################################################
####### Plot Mean Condensate Profile Liquid for entire simulation
############################################################
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(10,6),nrows=1,ncols=1)
cnt = 0
for model,TCL_i in TCL_CLN.items():  
    yaxis = TCL_i.coord('geopotential_height').points
    data = TCL_i.collapsed(('x','y','time'),MEAN).data
    plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model+' CLN')
    
for model,TCL_i in TCL_POL.items():  
    yaxis = TCL_i.coord('geopotential_height').points
    data = TCL_i.collapsed(('x','y','time'),MEAN).data
    plt.plot(data,yaxis/1000,color=color[model],linestyle='-',label=model+' POL')
    print('W vs. Height calculated and plotted for',model)

plt.ylim((0,15))
plt.legend()
plt.ylabel('Altitude (km)')
plt.xlabel('liquid mixing ratio (kg/kg)')
ax1.ticklabel_format(style='sci',axis='x', scilimits=(0,0))
plt.grid()
plt.tight_layout()

os.makedirs('Plots/Condensate',exist_ok=True)
plt.savefig(os.path.join('Plots','Condensate',savename+'TCL_prof.png'))
plt.close(fig1)

############################################################
####### Plot Mean Condensate Diff Profile Liquid for entire simulation
############################################################
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(10,6),nrows=1,ncols=1)
cnt = 0
for i,model in enumerate(models):
    yaxis = TCI_CLN[model].coord('geopotential_height').points
    data = TCL_POL[model].collapsed(('x','y','time'),MEAN).data-TCL_CLN[model].collapsed(('x','y','time'),MEAN).data

    plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model+'POL-CLN')
    plt.ylim((0,15))

plt.ylim((0,15))
plt.legend()
plt.ylabel('Altitude (km)')
plt.xlabel('liquid mixing ratio diff (kg/kg)')
plt.grid()
ax1.ticklabel_format(style='sci',axis='x', scilimits=(0,0))
plt.tight_layout()
os.makedirs('Plots/Condensate',exist_ok=True)
plt.savefig(os.path.join('Plots','Condensate',savename+'TCL_prof_diff.png'))
plt.close(fig1)


############################################################
####### Plot Mean Condensate Profile Ice for entire simulation
############################################################
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(10,6),nrows=1,ncols=1)
cnt = 0
for model,TCI_i in TCI_CLN.items():  
    yaxis = TCI_i.coord('geopotential_height').points
    data = TCI_i.collapsed(('x','y','time'),MEAN).data

    plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model+' CLN')
    
for model,TCI_i in TCI_POL.items():  
    yaxis = TCI_i.coord('geopotential_height').points
    data = TCI_i.collapsed(('x','y','time'),MEAN).data
    plt.plot(data,yaxis/1000,color=color[model],linestyle='-',label=model+' POL')
    print('Ice profile calculated and plotted for',model)

plt.ylim((0,15))
plt.legend()
plt.ylabel('Altitude (km)')
plt.xlabel('ice mixing ratio (kg/kg)')
plt.grid()
ax1.ticklabel_format(style='sci',axis='x', scilimits=(0,0))
plt.tight_layout()
os.makedirs('Plots/Condensate',exist_ok=True)
plt.savefig(os.path.join('Plots','Condensate',savename+'TCI_prof.png'))
plt.close(fig1)


############################################################
####### Plot Mean Condensate Diff Profile Ice for entire simulation
############################################################
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(6,4),nrows=1,ncols=1)
cnt = 0
for i,model in enumerate(models):
    yaxis = TCI_CLN[model].coord('geopotential_height').points
    data = TCI_POL[model].collapsed(('x','y','time'),MEAN).data-TCI_CLN[model].collapsed(('x','y','time'),MEAN).data

    plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model+'POL-CLN')
    plt.ylim((0,15))
    print('Ice diff profile calculated and plotted for',model)

plt.legend()
plt.ylabel('Altitude (km)')
plt.xlabel('ice mixing ratio (kg/kg)')
plt.grid()
plt.tight_layout()

os.makedirs('Plots/Condensate',exist_ok=True)
plt.savefig(os.path.join('Plots','Condensate',savename+'TCI_prof_diff.png'))
plt.close(fig1)
