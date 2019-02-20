import matplotlib.pyplot as plt
plt.switch_backend('agg')
from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict
f = lambda: defaultdict(f) 

import iris
import glob,os
from copy import deepcopy
import numpy as np
import datetime

from plot_functions.plot_functions import plot_2D_map
import cartopy.crs as ccrs

import warnings
warnings.filterwarnings('ignore', category=UserWarning, append=True)
warnings.filterwarnings('ignore', category=RuntimeWarning, append=True)
warnings.filterwarnings('ignore', category=FutureWarning, append=True)

models=[]
models.append('WRF_OXF')
models.append('RAMS_CSU')
models.append('COSMO_KIT')
models.append('UM_LEEDS')
models.append('WRF_NASA')

cases=['CLN','POL']

files=defaultdict(f)

for case in cases:
    for model in models:
        files[case]['500m']['1h'][model]=glob.glob(os.path.join(directory[case]['500m']['1h'][model],filename['500m']['1h'][model]))


Precip=defaultdict(f)
Precip_accum=defaultdict(f)

for case in cases:
    for model in models:
        if model is 'UM_LEEDS':
            Precip[case][model]=load_variable_cube[model](files[case]['500m']['1h'][model],variable_names[model]['AccumPrecip'])
            Precip_accum[case][model]=deepcopy(Precip[case][model])
            for i in range(1,Precip_accum[case][model].coord('time').shape[0]):
                Precip_accum[case][model][i].data=np.sum(Precip[case][model].core_data()[0:i],axis=0)

        else:
            Precip_accum[case][model]=load_variable_cube[model](files[case]['500m']['1h'][model],variable_names[model]['AccumPrecip'])
            Precip[case][model]=deepcopy(Precip_accum[case][model])
            Precip[case][model].data[1:]=Precip_accum[case][model].core_data()[1:]-Precip_accum[case][model].core_data()[:-1]


## restrict the Stage4 data to period where there is actually data in the cube
Stage4=iris.load_cube('/group_workspaces/jasmin2/acpc/houston_deep_convection/Stage4/Stage4.nc')[:,:,0:17]
Stage4_accum=deepcopy(Stage4)
Stage4_accum.units='kg m-2'
Stage4_accum.rename('Accumulated Precipitation')
for i in range(1,Stage4.coord('time').shape[0]):
    Stage4_accum.data[:,:,i]=np.sum(Stage4.core_data()[:,:,0:i],axis=2)


os.makedirs('Plots/Precip_Maps_hrly',exist_ok=True)
os.makedirs('Plots/Precip_Maps_hrly_accum',exist_ok=True)

times=[]
for hour in range(0,24):
    times.append(datetime.datetime(2013,6,19,12,0,0)+datetime.timedelta(hours=hour))


vmin=0
vmax=20
axes_extent=[-96.3,-93.9,28.4,30.5]
for case in cases:
    os.makedirs(os.path.join('Plots','Precip_Maps_hrly',case,'All'),exist_ok=True)
    for time in times:
        constraint_time=iris.Constraint(time=time)
        fig3,ax3=plt.subplots(nrows=2,ncols=3,figsize=(30/2.54,20/2.54),squeeze=False,subplot_kw={'projection': ccrs.PlateCarree()})
        ax3_flat=ax3.flatten()
        for i,model in enumerate(models):
            fig4,ax4=plt.subplots(nrows=1,ncols=1,figsize=(10/2.54,10/2.54),subplot_kw={'projection': ccrs.PlateCarree()})
            os.makedirs(os.path.join('Plots','Precip_Maps_hrly',case,model),exist_ok=True)
            Precip_i=Precip[case][model].extract(constraint_time)
            Stage4_i=Stage4.extract(constraint_time)

            if Precip_i is not None:
                plot_Precip_subplot=plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax3_flat[i],vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
                plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax4,vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
                fig4.savefig(os.path.join('Plots','Precip_Maps_hrly',case,model,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
            plt.close(fig4)
            if Stage4_i is not None:
                plot_Precip_subplot=plot_2D_map(Stage4_i,title='Stage4',axes_extent=axes_extent,axes=ax3_flat[5],vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
        fig3.savefig(os.path.join('Plots','Precip_Maps_hrly',case,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
        plt.close(fig3)
        
        
vmin=0
vmax=20
axes_extent=[-96.3,-93.9,28.4,30.5]
for case in cases:
    os.makedirs(os.path.join('Plots','Precip_Maps_hrly_accum',case,'All'),exist_ok=True)
    for time in times:
        constraint_time=iris.Constraint(time=time)
        fig3,ax3=plt.subplots(nrows=2,ncols=3,figsize=(30/2.54,20/2.54),squeeze=False,subplot_kw={'projection': ccrs.PlateCarree()})
        ax3_flat=ax3.flatten()
        for i,model in enumerate(models):
            fig4,ax4=plt.subplots(nrows=1,ncols=1,figsize=(10/2.54,10/2.54),subplot_kw={'projection': ccrs.PlateCarree()})
            os.makedirs(os.path.join('Plots','Precip_Maps_hrly_accum',case,model),exist_ok=True)
            Precip_i=Precip_accum[case][model].extract(constraint_time)
            Stage4_i=Stage4_accum.extract(constraint_time)

            if Precip_i is not None:
                plot_Precip_subplot=plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax3_flat[i],vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
                plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax4,vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
                fig4.savefig(os.path.join('Plots','Precip_Maps_hrly_accum',case,model,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
            plt.close(fig4)
            if Stage4_i is not None:
                plot_Precip_subplot=plot_2D_map(Stage4_i,title=model,axes_extent=axes_extent,axes=ax3_flat[5],vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,colorbar_label=False,cmap='Blues')
        fig3.savefig(os.path.join('Plots','Precip_Maps_hrly_accum',case,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
        plt.close(fig3)
print('done')
