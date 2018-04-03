import matplotlib.pyplot as plt
plt.switch_backend('agg')
from Setup_intercomparison import load_variable_cube,color,variable_names,directory,filename
from collections import defaultdict
f = lambda: defaultdict(f) 

import iris
import glob,os

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


OLR=defaultdict(f)
for case in cases:
    for model in models:
        OLR[case][model]=load_variable_cube[model](files[case]['500m']['1h'][model],variable_names[model]['OLR'])




os.makedirs('Plots/OLR_Maps',exist_ok=True)

times=[]
for hour in range(0,24):
    times.append(datetime.datetime(2013,6,19,12,0,0)+datetime.timedelta(hours=hour))

vmin=100
vmax=300
axes_extent=[-96.3,-93.9,28.4,30.5]

for case in cases:
    os.makedirs(os.path.join('Plots','OLR_Maps_hrly',case,'All'),exist_ok=True)
    for time in times:
        constraint_time=iris.Constraint(time=time)
        fig3,ax3=plt.subplots(nrows=3,ncols=2,figsize=(30/2.54,20/2.54),squeeze=False,subplot_kw={'projection': ccrs.PlateCarree()})
        ax3_flat=ax3.flatten()
        for i,model in enumerate(models):
            fig4,ax4=plt.subplots(nrows=1,ncols=1,figsize=(10/2.54,10/2.54),subplot_kw={'projection': ccrs.PlateCarree()})
            os.makedirs(os.path.join('Plots','OLR_Maps_hrly',case,model),exist_ok=True)
            OLR_i=OLR[case][model].extract(constraint_time)
            if OLR_i is not None:
                plot_OLR_subplot=plot_2D_map(OLR_i,title=model,axes_extent=axes_extent,axes=ax3_flat[i],vmin=vmin,vmax=vmax,n_levels=50,colorbar=False,cmap='viridis')
                plot_2D_map(OLR_i,title=model,axes_extent=axes_extent,axes=ax4,vmin=vmin,vmax=vmax,n_levels=50,colorbar=True,cmap='viridis')
                fig4.savefig(os.path.join('Plots','OLR_Maps_hrly',case,model,'OLR_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
            plt.close(fig4)
        fig3.colorbar(plot_OLR_subplot,orientation='horizontal')
        fig3.savefig(os.path.join('Plots','OLR_Maps_hrly',case,'OLR_Maps'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
        plt.close(fig3)

print('done')
