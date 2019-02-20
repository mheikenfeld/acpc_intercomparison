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
import datetime
# Import Python Libraries
import iris.plot as iplt
from iris.analysis import MEAN, MAX, SUM
import iris
import matplotlib
matplotlib.pyplot.switch_backend('agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict, OrderedDict
f = lambda: defaultdict(f) 

from dask.array.ma import masked_where
import warnings
warnings.filterwarnings('ignore', category=UserWarning, append=True)
warnings.filterwarnings('ignore', category=RuntimeWarning, append=True)
warnings.filterwarnings('ignore', category=FutureWarning, append=True)


savename = 'G3_hrly_b'


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
############## Load data for each model, using specified load module
#########################################################################   
def time_interval(cell):
    """Returns true if the model level is between X and Y"""
    return datetime.datetime(2013,6,19,21,0,0) <= cell <= datetime.datetime(2013,6,19,23,0,0)

constraint_time=iris.Constraint(time=time_interval)

MV_CLN=OrderedDict()
MV_POL=OrderedDict()
for model in models:
    MV_CLN[model]=load_variable_cube[model](files_CLN_500m_1h[model],variable_names[model]['W']).extract_cube(constraint_time)

    MV_POL[model]=load_variable_cube[model](files_POL_500m_1h[model],variable_names[model]['W']).extract_cube(constraint_time)




#########################################################################
####### PLOTTING
#########################################################################


############################################################
####### Plot Mean W Profile for entire simulation
############################################################
matplotlib.rcParams.update({'font.size': 14})
fig1,ax1=plt.subplots(figsize=(6,4),nrows=1,ncols=1)
cnt = 0
for model,W_i in MV_CLN.items():
    print(model)
    print(W_i)
    yaxis = W_i.coord('geopotential_height').points
    data = W_i.collapsed(('x','y','time'),MEAN).data
    
    plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model)
    plt.ylim((0,15))
    plt.legend()
    plt.ylabel('Altitude (km)')
    plt.xlabel('Mean Vertical Velocity (m/s)')
    plt.grid()
    print('W vs. Height calculated and plotted for',model)
plt.tight_layout()

os.makedirs('Plots/W',exist_ok=True)
plt.savefig(os.path.join('Plots','W',savename+'W_prof.png'))
plt.close(fig1)


############################################################
####### Plot Mean W Profile for entire simulation with threshold
############################################################

for w_thresh in [1,2,5]:
    matplotlib.rcParams.update({'font.size': 14})
    fig1,ax1=plt.subplots(figsize=(6,4),nrows=1,ncols=1)
    cnt = 0
    for model,W_i in MV_CLN.items():  
        yaxis = W_i.coord('geopotential_height').points
        W_i.data=masked_where(W_i.core_data()<w_thresh,W_i.core_data())
        data = W_i.collapsed(('x','y','time'),MEAN).data
    
        plt.plot(data,yaxis/1000,color=color[model],linestyle='--',label=model)
        plt.ylim((0,15))
        plt.legend()
        plt.ylabel('Altitude (km)')
        plt.xlabel('Mean Vertical Velocity (m/s)')
        plt.grid()
        print('W vs. Height calculated and plotted for',model)
    plt.tight_layout()
    os.makedirs('Plots/W',exist_ok=True)
    plt.savefig(os.path.join('Plots','W',savename+'W_prof_threshold_'+ str(w_thresh)+'.png'))
    plt.close(fig1)

# ##########################################################################
# ####### Plot Mean W Profile versus Time for all the models
# ##########################################################################
# init_date = datetime.datetime(1970, 1, 1, 0, 0, 0)

# cntrs = np.arange(-0.03,0.03,0.002)
# matplotlib.rcParams.update({'font.size': 12})
# fig1,ax1=plt.subplots(figsize=(12,10),nrows=len(models),ncols=2)
# cnt = 0
# for model,W_i in MV_CLN.items():  
#     print('W vs. Height/Time calculated and plotted for',model)

#     xaxis = W_i.coord('time').points
#     xaxis_date = []
#     for i in np.arange(0,len(xaxis)):
#         xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))

#     yaxis = W_i.coord('geopotential_height').points
#     data = W_i.collapsed(('x','y'),MEAN).data
#     z_plot = ax1[cnt,0].contourf(xaxis_date,yaxis/1000,np.transpose(data),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#     plt.colorbar(z_plot,ax=ax1[cnt,0])
#     ax1[cnt,0].set_title(model+'-CLN')
#     ax1[cnt,0].set_ylim((0,15))
#     myFmt = mdates.DateFormatter('%H:%M')
#     ax1[cnt,0].xaxis.set_major_formatter(myFmt)
#     ax1[cnt,0].set_ylabel('Geopot. Height (km)')
#     ax1[cnt,0].grid()
#     cnt = cnt + 1
#     plt.grid()

# ax1[cnt-1,0].set_xlabel('Time (UTC)')

# cnt = 0
# for model,W_i in MV_POL.items():  
#     print('W vs. Height/Time calculated and plotted for',model)

#     xaxis = W_i.coord('time').points
#     xaxis_date = []
#     for i in np.arange(0,len(xaxis)):
#         xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))

#     yaxis = W_i.coord('geopotential_height').points
#     data = W_i.collapsed(('x','y'),MEAN).data
#     z_plot = ax1[cnt,1].contourf(xaxis_date,yaxis/1000,np.transpose(data),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#     plt.colorbar(z_plot,ax=ax1[cnt,1])
#     ax1[cnt,1].set_title(model+'-POL')
#     ax1[cnt,1].set_ylim((0,15))
#     myFmt = mdates.DateFormatter('%H:%M')
#     ax1[cnt,1].xaxis.set_major_formatter(myFmt)
#     ax1[cnt,1].grid()
#     cnt = cnt + 1

# ax1[cnt-1,1].set_xlabel('Time (UTC)')
# plt.tight_layout()

# os.makedirs('Plots/W',exist_ok=True)
# plt.savefig(os.path.join('Plots','W',savename+'W_prof_time_nothresh.png'))
# plt.close(fig1)

# ##########################################################################
# ####### Plot Mean W Updraft Profile versus Time for all the models
# ####### Threshhold on W
# ##########################################################################
# init_date = datetime.datetime(1970, 1, 1, 0, 0, 0)

# for w_thresh in (0,1,3,5,7,10):
#     cntrs = np.arange(w_thresh,15,1)
    
#     matplotlib.rcParams.update({'font.size': 12})
#     fig1,ax1=plt.subplots(figsize=(30,30),nrows=len(models),ncols=4)
#     cnt = 0
#     for model,W_i in MV_CLN.items():  
#         print('W vs. Height/Time calculated and plotted for',model)
    
#         xaxis = W_i.coord('time').points
#         xaxis_date = []
#         for i in np.arange(0,len(xaxis)):
#             xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))
    
#         yaxis = W_i.coord('geopotential_height').points
    
#         # Calculate mean profiles and number of points that meet threshold at each model timestep
#         plot_data_cln = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
#         plot_data_num_cln = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
        
#         for t in np.arange(0,W_i.shape[0]):
#             data = W_i[t,:,:,:].data
#             data[data < w_thresh] = np.nan
#             data = np.reshape(data,(W_i.shape[1],W_i.shape[2]*W_i.shape[3]))
#             data_prof = np.nanmean(data,axis=1)        
#             data_prof_num = np.zeros(W_i.shape[1])        
#             for z in np.arange(0,W_i.shape[1]):           
#                 data_prof_num[z] = np.count_nonzero(~np.isnan(data[z,:]),axis=0)
    
#             plot_data_cln[t,:,cnt] = data_prof
#             plot_data_num_cln[t,:,cnt] = data_prof_num
    
    
#         z_plot = ax1[cnt,0].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_cln[:,0:len(yaxis),cnt]),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#         plt.colorbar(z_plot,ax=ax1[cnt,0])
#         ax1[cnt,0].xaxis_date()
#         ax1[cnt,0].set_title(model+'-CLN')
#         ax1[cnt,0].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,0].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,0].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,0].grid()
#         plt.grid()
    
#         z_plot = ax1[cnt,2].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_num_cln[:,0:len(yaxis),cnt]))
#         plt.colorbar(z_plot,ax=ax1[cnt,2])
#         ax1[cnt,2].xaxis_date()
#         ax1[cnt,2].set_title(model+'-CLN')
#         ax1[cnt,2].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,2].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,2].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,2].grid()
#         plt.grid()
    
#         cnt = cnt + 1
    
    
#     ax1[cnt-1,0].set_xlabel('Time (UTC)')
    
#     cnt = 0
#     for model,W_i in MV_POL.items():  
#         print('W vs. Height/Time calculated and plotted for',model)
    
#         xaxis = W_i.coord('time').points
#         xaxis_date = []
#         for i in np.arange(0,len(xaxis)):
#             xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))
    
#         yaxis = W_i.coord('geopotential_height').points
    
#         plot_data_pol = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
#         plot_data_num_pol = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
    
#         for t in np.arange(0,W_i.shape[0]):
#             data = W_i[t,:,:,:].data
#             data[data < w_thresh] = np.nan
#             data = np.reshape(data,(W_i.shape[1],W_i.shape[2]*W_i.shape[3]))
#             data_prof = np.nanmean(data,axis=1)        
#             data_prof_num = np.zeros(W_i.shape[1])        
#             for z in np.arange(0,W_i.shape[1]):           
#                 data_prof_num[z] = np.count_nonzero(~np.isnan(data[z,:]),axis=0)
    
#             plot_data_pol[t,:,cnt] = data_prof
#             plot_data_num_pol[t,:,cnt] = data_prof_num
    
#         z_plot = ax1[cnt,1].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_pol[:,0:len(yaxis),cnt]),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#         plt.colorbar(z_plot,ax=ax1[cnt,1])
#         ax1[cnt,1].xaxis_date()
#         ax1[cnt,1].set_title(model+'-POL')
#         ax1[cnt,1].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,1].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,1].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,1].grid()
#         plt.grid()
    
#         z_plot = ax1[cnt,3].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_num_pol[:,0:len(yaxis),cnt]))
#         plt.colorbar(z_plot,ax=ax1[cnt,3])
#         ax1[cnt,3].xaxis_date()
#         ax1[cnt,3].set_title(model+'-POL')
#         ax1[cnt,3].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,3].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,3].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,3].grid()
#         plt.grid()
    
#         cnt = cnt + 1
    
    
#     ax1[cnt-1,0].set_xlabel('Time (UTC)')
#     plt.tight_layout()
    
#     os.makedirs('Plots/W',exist_ok=True)
#     plt.savefig(os.path.join('Plots','W',savename+'_W_prof_time_Wthresh_'+str(w_thresh)+'.png'))
#     plt.close(fig1)


# ##########################################################################
# ####### Plot Mean W Updraft Profile versus Time for all the models
# ####### Threshhold on W and TC
# ##########################################################################

# init_date = datetime.datetime(1970, 1, 1, 0, 0, 0)

# for w_thresh in (0,1,3,5,7,10):
#     cntrs = np.arange(w_thresh,15,1)
#     tc_thresh = 0.00001 # 0.01 g/kg threshold
    
#     matplotlib.rcParams.update({'font.size': 12})
#     fig1,ax1=plt.subplots(figsize=(30,30),nrows=len(models),ncols=4)
#     cnt = 0
#     for model,W_i in MV_CLN.items():  
#         print('W vs. Height/Time calculated and plotted for',model)
    
#         xaxis = W_i.coord('time').points
#         xaxis_date = []
#         for i in np.arange(0,len(xaxis)):
#             xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))
    
#         yaxis = W_i.coord('geopotential_height').points
    
#         # Calculate mean profiles and number of points that meet threshold at each model timestep
#         plot_data_cln = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
#         plot_data_num_cln = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
        
#         for t in np.arange(0,W_i.shape[0]):
#             data = W_i[t,:,:,:].data
#             data_TC = TC_CLN[model][t,:,:,:].data
#             data[data < w_thresh] = np.nan
#             data[data_TC < tc_thresh] = np.nan
#             data = np.reshape(data,(W_i.shape[1],W_i.shape[2]*W_i.shape[3]))
#             data_prof = np.nanmean(data,axis=1)        
#             data_prof_num = np.zeros(W_i.shape[1])        
#             for z in np.arange(0,W_i.shape[1]):           
#                 data_prof_num[z] = np.count_nonzero(~np.isnan(data[z,:]),axis=0)
    
#             plot_data_cln[t,:,cnt] = data_prof
#             plot_data_num_cln[t,:,cnt] = data_prof_num
    
#         z_plot = ax1[cnt,0].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_cln[:,0:len(yaxis),cnt]),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#         plt.colorbar(z_plot,ax=ax1[cnt,0])
#         ax1[cnt,0].xaxis_date()
#         ax1[cnt,0].set_title(model+'-CLN')
#         ax1[cnt,0].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,0].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,0].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,0].grid()
#         plt.grid()
        
#         z_plot = ax1[cnt,2].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_num_cln[:,0:len(yaxis),cnt]))
#         plt.colorbar(z_plot,ax=ax1[cnt,2])
#         ax1[cnt,2].xaxis_date()
#         ax1[cnt,2].set_title(model+'-CLN')
#         ax1[cnt,2].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,2].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,2].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,2].grid()
#         plt.grid()
    
#         cnt = cnt + 1
    
#     ax1[cnt-1,0].set_xlabel('Time (UTC)')
    
#     cnt = 0
#     for model,W_i in MV_POL.items():  
#         print('W vs. Height/Time calculated and plotted for',model)
    
#         xaxis = W_i.coord('time').points
#         xaxis_date = []
#         for i in np.arange(0,len(xaxis)):
#             xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))
    
#         yaxis = W_i.coord('geopotential_height').points
    
#         plot_data_pol = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
#         plot_data_num_pol = np.zeros((W_i.shape[0],W_i.shape[1],len(models)))
    
#         for t in np.arange(0,W_i.shape[0]):
#             data = W_i[t,:,:,:].data
#             data_TC = TC_POL[model][t,:,:,:].data
#             data[data < w_thresh] = np.nan
#             data[data_TC < tc_thresh] = np.nan
#             data = np.reshape(data,(W_i.shape[1],W_i.shape[2]*W_i.shape[3]))
#             data_prof = np.nanmean(data,axis=1)        
#             data_prof_num = np.zeros(W_i.shape[1])        
#             for z in np.arange(0,W_i.shape[1]):           
#                 data_prof_num[z] = np.count_nonzero(~np.isnan(data[z,:]),axis=0)
    
#             plot_data_pol[t,:,cnt] = data_prof
#             plot_data_num_pol[t,:,cnt] = data_prof_num
    
#         z_plot = ax1[cnt,1].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_pol[:,0:len(yaxis),cnt]),levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#         plt.colorbar(z_plot,ax=ax1[cnt,1])
#         ax1[cnt,1].xaxis_date()
#         ax1[cnt,1].set_title(model+'-POL')
#         ax1[cnt,1].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,1].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,1].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,1].grid()
#         plt.grid()
    
#         z_plot = ax1[cnt,3].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_num_pol[:,0:len(yaxis),cnt]))
#         plt.colorbar(z_plot,ax=ax1[cnt,3])
#         ax1[cnt,3].xaxis_date()
#         ax1[cnt,3].set_title(model+'-POL')
#         ax1[cnt,3].set_ylim((0,15))
#         myFmt = mdates.DateFormatter('%H:%M')
#         ax1[cnt,3].xaxis.set_major_formatter(myFmt)
#         ax1[cnt,3].set_ylabel('Geopot. Height (km)')
#         ax1[cnt,3].grid()
#         plt.grid()
    
#         cnt = cnt + 1
        
#     ax1[cnt-1,0].set_xlabel('Time (UTC)')
#     plt.tight_layout()
    
#     os.makedirs('Plots/W',exist_ok=True)
#     plt.savefig(os.path.join('Plots','W',savename+'_W_prof_time_Wthresh_'+str(w_thresh)+'_TCthresh_'+str(tc_thresh)+'.png'),dpi=600)
#     plt.close(fig1)

# ############################################################
# ####### Plot Mean TC within Updraft Profile versus Time for all the models
# ####### Threshhold on W and TC
# ############################################################
# init_date = datetime.datetime(1970, 1, 1, 0, 0, 0)

# w_thresh = 3
# tc_thresh = 0.00001 # 0.01 g/kg threshold
# cntrs = np.arange(0.1,5,0.2)
# matplotlib.rcParams.update({'font.size': 12})
# fig1,ax1=plt.subplots(figsize=(12,10),nrows=len(models),ncols=2)
# cnt = 0
# for model,W_i in MV_CLN.items():  
#     print('W vs. Height/Time calculated and plotted for',model)

#     xaxis = W_i.coord('time').points
#     xaxis_date = []
#     for i in np.arange(0,len(xaxis)):
#         xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))
        
#     yaxis = TC_CLN[model].coord('geopotential_height').points

#     # Calculate mean profiles and number of points that meet threshold at each model timestep
#     plot_data_cln = np.zeros((TC_CLN[model].shape[0],TC_CLN[model].shape[1],len(models)))
#     plot_data_num_cln = np.zeros((TC_CLN[model].shape[0],TC_CLN[model].shape[1],len(models)))
    
#     for t in np.arange(0,TC_CLN[model].shape[0]):
#         data = W_i[t,:,:,:].data
#         data_TC = TC_CLN[model][t,:,:,:].data
#         data_TC[data[0:np.shape(data_TC)[0],:,:] < w_thresh] = np.nan
#         data_TC[data_TC < tc_thresh] = np.nan
#         data_TC = np.reshape(data_TC,(TC_CLN[model].shape[1],TC_CLN[model].shape[2]*TC_CLN[model].shape[3]))
#         data_prof = np.nanmean(data_TC,axis=1)        
#         data_prof_num = np.zeros(TC_CLN[model].shape[1])        
#         for z in np.arange(0,TC_CLN[model].shape[1]):           
#             data_prof_num[z] = np.count_nonzero(~np.isnan(data_TC[z,:]),axis=0)

#         plot_data_cln[t,:,cnt] = data_prof
#         plot_data_num_cln[t,:,cnt] = data_prof_num

#     z_plot = ax1[cnt,0].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_cln[:,0:len(yaxis),cnt])*1000,levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#     plt.colorbar(z_plot,ax=ax1[cnt,0])
#     ax1[cnt,0].xaxis_date()
#     ax1[cnt,0].set_title(model+'-CLN')
#     ax1[cnt,0].set_ylim((0,15))
#     myFmt = mdates.DateFormatter('%H:%M')
#     ax1[cnt,0].xaxis.set_major_formatter(myFmt)
#     ax1[cnt,0].set_ylabel('Geopot. Height (km)')
#     ax1[cnt,0].grid()
#     cnt = cnt + 1
#     plt.grid()

# ax1[cnt-1,0].set_xlabel('Time (UTC)')

# cnt = 0
# for model,W_i in MV_POL.items():  
#     print('W vs. Height/Time calculated and plotted for',model)

#     xaxis = W_i.coord('time').points
#     xaxis_date = []
#     for i in np.arange(0,len(xaxis)):
#         xaxis_date.append(init_date+datetime.timedelta(days=xaxis[i]))

#     yaxis = TC_POL[model].coord('geopotential_height').points

#     # Calculate mean profiles and number of points that meet threshold at each model timestep
#     plot_data_pol = np.zeros((TC_POL[model].shape[0],TC_POL[model].shape[1],len(models)))
#     plot_data_num_pol = np.zeros((TC_POL[model].shape[0],TC_POL[model].shape[1],len(models)))
    
#     for t in np.arange(0,TC_POL[model].shape[0]):
#         data = W_i[t,:,:,:].data
#         data_TC = TC_POL[model][t,:,:,:].data
#         data_TC[data[0:np.shape(data_TC)[0],:,:] < w_thresh] = np.nan
#         data_TC[data_TC < tc_thresh] = np.nan
#         data_TC = np.reshape(data_TC,(TC_POL[model].shape[1],TC_POL[model].shape[2]*TC_POL[model].shape[3]))
#         data_prof = np.nanmean(data_TC,axis=1)        
#         data_prof_num = np.zeros(TC_POL[model].shape[1])        
#         for z in np.arange(0,TC_CLN[model].shape[1]):           
#             data_prof_num[z] = np.count_nonzero(~np.isnan(data_TC[z,:]),axis=0)

#         plot_data_pol[t,:,cnt] = data_prof
#         plot_data_num_pol[t,:,cnt] = data_prof_num

#     z_plot = ax1[cnt,1].contourf(xaxis_date,yaxis/1000,np.transpose(plot_data_pol[:,0:len(yaxis),cnt])*1000,levels=cntrs,vmin=np.nanmin(cntrs),vmax=np.nanmax(cntrs))
#     plt.colorbar(z_plot,ax=ax1[cnt,1])
#     ax1[cnt,1].xaxis_date()
#     ax1[cnt,1].set_title(model+'-POL')
#     ax1[cnt,1].set_ylim((0,15))
#     myFmt = mdates.DateFormatter('%H:%M')
#     ax1[cnt,1].xaxis.set_major_formatter(myFmt)
#     ax1[cnt,1].set_ylabel('Geopot. Height (km)')
#     ax1[cnt,1].grid()
#     cnt = cnt + 1
#     plt.grid()

# ax1[cnt-1,0].set_xlabel('Time (UTC)')
# plt.tight_layout()

# os.makedirs('Plots/W',exist_ok=True)
# plt.savefig(os.path.join('Plots','W',savename+'_TC_prof_time_Wthresh_'+str(w_thresh)+'_TCthresh_'+str(tc_thresh)+'.png'),dpi=600)
# plt.close(fig1)
