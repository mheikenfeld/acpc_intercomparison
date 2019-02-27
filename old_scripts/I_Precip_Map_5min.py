import matplotlib.pyplot as plt
plt.switch_backend('agg')
from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict
f = lambda: defaultdict(f) 
from copy import deepcopy
import iris
import glob,os
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
        files[case]['500m']['5m'][model]=glob.glob(os.path.join(directory[case]['500m']['5m'][model],filename['500m']['5m'][model]))


Precip=defaultdict(f)
Precip_accum=defaultdict(f)

for case in cases:
    for model in models:
        if model is 'UM_LEEDS':
            Precip[case][model]=load_variable_cube[model](files[case]['500m']['5m'][model],variable_names[model]['AccumPrecip'])
            Precip_accum[case][model]=deepcopy(Precip[case][model])
            for i in range(1,Precip_accum[case][model].coord('time').shape[0]):
                Precip_accum[case][model][i].data=np.sum(Precip.core_data()[0:i],axis=0)

        else:
            Precip_accum[case][model]=load_variable_cube[model](files[case]['500m']['5m'][model],variable_names[model]['AccumPrecip'])
            Precip[case][model]=deepcopy(Precip_accum[case][model])
            Precip[case][model].data[1:]=Precip[case][model][1:].core_data()-Precip[case][model][:-1].core_data()


os.makedirs('Plots/Precip_Maps',exist_ok=True)

times=[]
for minute in range(0,5*10*12,5):
    times.append(datetime.datetime(2013,6,19,16,0,0)+datetime.timedelta(minutes=minute))

vmin=0
vmax=20
axes_extent=[-96.3,-93.9,28.4,30.5]

for case in cases:
    os.makedirs(os.path.join('Plots','Precip_Maps',case,'All'),exist_ok=True)
    for time in times:
        constraint_time=iris.Constraint(time=time)
        fig3,ax3=plt.subplots(nrows=3,ncols=2,figsize=(30/2.54,20/2.54),squeeze=False,subplot_kw={'projection': ccrs.PlateCarree()})
        ax3_flat=ax3.flatten()
        for i,model in enumerate(models):
            fig4,ax4=plt.subplots(nrows=1,ncols=1,figsize=(10/2.54,10/2.54),subplot_kw={'projection': ccrs.PlateCarree()})
            os.makedirs(os.path.join('Plots','Precip_Maps_5min',case,model),exist_ok=True)
            Precip_i=Precip[case][model].extract(constraint_time)
            print(model,Precip_i)
            if Precip_i is not None:
                plot_Precip_subplot=plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax3_flat[i],vmin=vmin,vmax=vmax,n_levels=50,colorbar=False,cmap='Blues')
                plot_2D_map(Precip_i,title=model,axes_extent=axes_extent,axes=ax4,vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,cmap='Blues')
                fig4.savefig(os.path.join('Plots','Precip_Maps_5min',case,model,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
            plt.close(fig4)
        fig3.colorbar(plot_Precip_subplot,orientation='horizontal')
        fig3.savefig(os.path.join('Plots','Precip_Maps_5min',case,'Precip_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
        plt.close(fig3)
print('done')
