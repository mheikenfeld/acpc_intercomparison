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
import datetime
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

import warnings
warnings.filterwarnings('ignore', category=UserWarning, append=True)
warnings.filterwarnings('ignore', category=RuntimeWarning, append=True)
warnings.filterwarnings('ignore', category=FutureWarning, append=True)


# from plot_functions.plot_functions import plot_2D_map

models=[]
models.append('WRF_OXF')
models.append('RAMS_CSU')
models.append('COSMO_KIT')
models.append('UM_LEEDS')
models.append('WRF_NASA')


savename = 'G3_5m_'

######################################################    
# use short subset of data files from each model for testing:
#filename=filename_test

# Get filename paths for all the data
files_CLN_500m_5min=OrderedDict(); files_POL_500m_5min=OrderedDict()
for model in models:
    # print(os.path.join(directory['CLN']['500m']['5m'][model],filename['500m'][model]))
    files_CLN_500m_5min[model]=glob.glob(os.path.join(directory['CLN']['500m']['5m'][model],filename['500m']['5m'][model]))
    # print(os.path.join(directory['POL']['500m']['5m'][model],filename['500m'][model]))
    files_POL_500m_5min[model]=glob.glob(os.path.join(directory['POL']['500m']['5m'][model],filename['500m']['5m'][model]))
       
#########################################################################    
############## Load data for each model, using specified load module
#########################################################################   
MV_CLN=OrderedDict()
MV_POL=OrderedDict()
for model in models:
    # print(model,files_CLN_500m_5min[model])
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
           W_i.collapsed(('x','y'),MEAN),
           axes=ax1,color=color[model],linestyle='--',label=model+'_CLN')
    else:
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),MEAN),
           axes=ax1,color=color[model],linestyle='--',label=model+'_CLN')

    print('Accumulated Precip vs. Time calculated and plotted for',model)

for model,W_i in MV_POL.items():  
    if model == 'UM_LEEDS':
        W_i.data = np.cumsum(W_i.data, axis=0); # Make Cumulative Sum
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),MEAN),
           axes=ax1,color=color[model],linestyle='-',label=model+'_POL')
    else:
        iplt.plot(W_i.coord('time'),
           W_i.collapsed(('x','y'),MEAN),
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
    
bins = [0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,15,20,50,100]
for model,W_i in MV_CLN.items():  
    
    data =  np.diff(W_i.data,axis=0)*60/5 #multipy to go to hourly rates
    data[data<0.001] = 0;
    h, bin_edges = np.histogram(data,bins,density=True)
    bin_mids = (bin_edges[0:len(bin_edges)-1]+bin_edges[1:])/2
    plt.plot(bin_mids,h,color=color[model],linestyle='--',label=model+'_CLN')

for model,W_i in MV_POL.items():  
    
    data = W_i.data; data = np.diff(data,axis=0)
    data[data<0.001] = 0;
    h, bin_edges = np.histogram(data,bins,density=True)
    bin_mids = (bin_edges[0:len(bin_edges)-1]+bin_edges[1:])/2

    plt.plot(bin_mids,h,color=color[model],linestyle='-',label=model+'_POL')

ax1.set_xscale('log')
#ax1.set_yscale('log')
ax1.set_xlabel('Hourly Precipitation Rate (kg m$^{-2}$ hr$^{-1}$)')
ax1.set_ylabel('Frequency')
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


