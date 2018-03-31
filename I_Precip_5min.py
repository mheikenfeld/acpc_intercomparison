#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:25:41 2018

@author: pmarin
# Code for Intermodel Comparsion for accumulated precipitation
# Started by M.H., editted by PJM (3/21/18)
"""
import numpy as np
import glob
import os
from datetime import datetime
# Import Python Libraries
import iris.plot as iplt
from iris.analysis import MEAN, MAX, SUM
import cartopy.crs as ccrs

import matplotlib
matplotlib.pyplot.switch_backend('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict, OrderedDict
f = lambda: defaultdict(f) 
# from plot_functions.plot_functions import plot_2D_map

# For PJM Local Testing
#import sys
#sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/wrfcube")
#sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ramscube")

# from load_models_PJM.load_WRF import load_WRF
# from load_models_PJM.load_RAMS import load_RAMS
# from load_models_PJM.load_COSMO import load_COSMO
# from load_models_PJM.load_UM import load_UM

######################################################    
############## Specify models, filenames, paths, etc..
######################################################
# Specify which load module to use for each model
# load_variable_cube=OrderedDict()
# load_variable_cube['WRF_OXF']=load_WRF
# load_variable_cube['WRF_NASA']=load_WRF
# load_variable_cube['WRF_HIJU']=load_WRF
# load_variable_cube['RAMS_CSU']=load_RAMS
# load_variable_cube['COSMO_KIT']=load_COSMO
# load_variable_cube['UM_LEEDS']=load_UM

# Specify colors for the models
# color=OrderedDict()
# color['WRF_OXF']='#002147'
# color['WRF_HIJU']='#77d8d8'
# color['WRF_NASA']='#0B3D91'
# color['RAMS_CSU']='#1E4D2B'
# color['COSMO_KIT']='#009682'
# color['UM_LEEDS']='#b31b1b'

# variable_names=OrderedDict()
# variable_names['WRF_OXF']=OrderedDict()
# variable_names['WRF_NASA']=OrderedDict()
# variable_names['WRF_HIJU']=OrderedDict()
# variable_names['RAMS_CSU']=OrderedDict()
# variable_names['COSMO_KIT']=OrderedDict()
# variable_names['UM_LEEDS']=OrderedDict()

# Specify variable name and unique variable id for each model
# new_varname = 'AccumPrecip'
# variable_names['WRF_OXF'][new_varname]='RAINNC'
# variable_names['RAMS_CSU'][new_varname]='ACCPR'
# variable_names['COSMO_KIT'][new_varname]='precipitation_amount'
# variable_names['UM_LEEDS'][new_varname]='pcp_accum'
# variable_names['WRF_NASA'][new_varname]='RAINNC'


# filename_500m=OrderedDict()
# filename_500m['WRF_OXF']="wrfout_d03*"
# filename_500m['RAMS_CSU']="a-A*-g3.h5"
# filename_500m['COSMO_KIT']="lfff*0000.nc_5min"
# filename_500m['UM_LEEDS']="*201306*.nc"
# filename_500m['WRF_NASA']="wrfout_d03*"

# directory_CLN_500m_5min=OrderedDict()
# directory_CLN_500m_5min['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/CLN/WRF_ACPC_201306191800_1h1h5min_CLN/d03"
# directory_CLN_500m_5min['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/CLN/x.out.5m"
# directory_CLN_500m_5min['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/CLN/500m"
# directory_CLN_500m_5min['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/CLN/0p5km_5m"
# directory_CLN_500m_5min['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_CLN"

# directory_POL_500m_5min=OrderedDict()
# directory_POL_500m_5min['WRF_OXF']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_Oxford/POL/WRF_ACPC_201306191800_1h1h5min_POL/d03"
# directory_POL_500m_5min['RAMS_CSU']="/group_workspaces/jasmin2/acpc/houston_deep_convection/RAMS_CSU/POL/x.out.5m"
# directory_POL_500m_5min['COSMO_KIT']="/group_workspaces/jasmin2/acpc/houston_deep_convection/COSMO_KIT/POL/500m"
# directory_POL_500m_5min['UM_LEEDS']="/group_workspaces/jasmin2/acpc/houston_deep_convection/UM_Leeds/POL/0p5km_5m"
# directory_POL_500m_5min['WRF_NASA']="/group_workspaces/jasmin2/acpc/houston_deep_convection/WRF_GISS/P3_POL"

models=[]
models.append('WRF_OXF')
models.append('RAMS_CSU')
models.append('COSMO_KIT')
models.append('UM_LEEDS')
models.append('WRF_NASA')

savename = 'G3_5m_'

######################################################    

# Get filename paths for all the data
files_CLN_500m_5min=OrderedDict(); files_POL_500m_5min=OrderedDict()
for model in models:
    # print(os.path.join(directory['CLN']['500m']['5min'][model],filename['500m'][model]))
    files_CLN_500m_5min[model]=glob.glob(os.path.join(directory['CLN']['500m']['5m'][model],filename['500m'][model]))
    # print(os.path.join(directory['POL']['500m']['5min'][model],filename['500m'][model]))
    files_POL_500m_5min[model]=glob.glob(os.path.join(directory['POL']['500m']['5m'][model],filename['500m'][model]))
       
#########################################################################    
############## Load data for each model, using specified load module
#########################################################################   
MV_CLN=OrderedDict()
MV_POL=OrderedDict()
for model in models:
    print(model,files_CLN_500m_5min[model])
    MV_CLN[model]=load_variable_cube[model](files_CLN_500m_5min[model],variable_names[model]['AccumPrecip'])
    MV_POL[model]=load_variable_cube[model](files_POL_500m_5min[model],variable_names[model]['AccumPrecip'])

################
####### PLOTTING
################

matplotlib.rcParams.update({'font.size': 12})
fig1,ax1=plt.subplots(figsize=(9,4),nrows=1,ncols=1)
for model,W_i in MV_CLN.items():  
    if model == 'UM_LEEDS':
        W_i.data = np.cumsum(W_i.data, axis=0); # Make Cumulative Sum
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),SUM),
           axes=ax1,color=color[model],linestyle='--',label=model+'_CLN')
    else:
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),SUM),
           axes=ax1,color=color[model],linestyle='--',label=model+'_CLN')

    print('Accumulated Precip vs. Time calculated and plotted for',model)

for model,W_i in MV_POL.items():  
    if model == 'UM_LEEDS':
        W_i.data = np.cumsum(W_i.data, axis=0); # Make Cumulative Sum
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),SUM),
           axes=ax1,color=color[model],linestyle='-',label=model+'_POL')
    else:
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),SUM),
           axes=ax1,color=color[model],linestyle='-',label=model+'_POL')

    print('Accumulated Precip vs. Time calculated and plotted for',model)

myFmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(myFmt)
ax1.set_ylabel('Accumulated Precipitation \n (kg m$^{-2}$)')
ax1.set_xlabel('Time (UTC)')
ax1.legend(prop={'size': 10})
plt.tight_layout()
plt.grid()

os.makedirs('Plots/PCP',exist_ok=True)
fig1.savefig(os.path.join('Plots','PCP',savename+'AccumPrecip'+'_Time.png'),dpi=600)

# Plot Hourly Precipitation Rate Histograms
# Since cum sum for UM_LEEDS was already done in the first plot, no need to do it again
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(7,5),nrows=1,ncols=1)
for model,W_i in MV_CLN.items():  
    
    data = W_i.data; data = np.diff(data,axis=0)
    data[data<0.001] = 0;
    bins = [0.001,0.01,0.05,0.1,0.5,1,5,10,15,20,50,100]
    h, bin_edges = np.histogram(data,bins)
    bin_mids = (bin_edges[0:len(bin_edges)-1]+bin_edges[1:])/2

    plt.plot(bin_mids,h,color=color[model],linestyle='--',label=model+'_CLN')

for model,W_i in MV_POL.items():  
    
    data = W_i.data; data = np.diff(data,axis=0)
    data[data<0.001] = 0;
    bins = [0.001,0.01,0.05,0.1,0.5,1,5,10,15,20,50,100]
    h, bin_edges = np.histogram(data,bins)
    bin_mids = (bin_edges[0:len(bin_edges)-1]+bin_edges[1:])/2

    plt.plot(bin_mids,h,color=color[model],linestyle='-',label=model+'_POL')

ax1.set_xscale('log')
#ax1.set_yscale('log')
ax1.set_xlabel('Hourly Precipitation Rate (kg m$^{-2}$ hr$^{-1}$)')
ax1.set_ylabel('Number of Grid Points')
ax1.legend()
plt.tight_layout()
plt.grid()

os.makedirs('Plots/PCP',exist_ok=True)
fig1.savefig(os.path.join('Plots','PCP',savename+'AccumPrecip'+'_Hist.png'),dpi=600)

# Plot Maximum Precipitation Rate at each time
# Precipitate Rate calculated as time differences in cumulative precipitation
init_date = datetime.datetime(1970, 1, 1, 0, 0, 0)

matplotlib.rcParams.update({'font.size': 12})
fig1,ax1=plt.subplots(figsize=(9,4),nrows=1,ncols=1)
for model,W_i in MV_CLN.items():  
    
    data = W_i.data; data = np.diff(data,axis=0)
    data = np.max(np.max(data,axis=2),axis=1)

    xaxis = W_i.coord('time').points
    xaxis_date = []
    for i in np.arange(0,len(xaxis)):
        xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))

    ax1.plot(xaxis_date[1:],data,color = color[model],linestyle='--',label=model+'_CLN')

for model,W_i in MV_POL.items():  
    
    data = W_i.data; data = np.diff(data,axis=0)
    data = np.max(np.max(data,axis=2),axis=1)
    
    xaxis = W_i.coord('time').points
    xaxis_date = []
    for i in np.arange(0,len(xaxis)):
        xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))

    ax1.plot(xaxis_date[1:],data,color = color[model],linestyle='-',label=model+'_POL')

ax1.legend()
myFmt = mdates.DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(myFmt)
ax1.set_yscale('log')
ax1.set_xlabel('Time (DD HH:MM UTC)')
ax1.set_ylabel('Precipitation Rate (mm hr$^{-1}$)')

ax1.set_ylim((0.1,200))
ax1.legend()
plt.tight_layout()
plt.grid()
    
os.makedirs('Plots/PCP',exist_ok=True)
fig1.savefig(os.path.join('Plots','PCP',savename+'AccumPrecip'+'_MAX_PCPRATE.png'),dpi=600)


