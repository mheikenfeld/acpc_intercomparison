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
# models.append('UM_LEEDS')
models.append('WRF_NASA')

cases=['CLN','POL']

files=defaultdict(f)

for case in cases:
    for model in models:
        # print(case)
        # print(model)
        # print(directory[case]['500m']['5m'][model])
        # print(filename['5m']['500m'][model])
        files[case]['500m']['5m'][model]=glob.glob(os.path.join(directory[case]['500m']['5m'][model],filename['500m']['5m'][model]))


OLR=defaultdict(f)
for case in cases:
    for model in models:
        # print(model,files[case]['500m']['5m'][model])
        OLR[case][model]=load_variable_cube[model](files[case]['500m']['5m'][model],variable_names[model]['OLR'])

print('OLR data loaded into cubes')



os.makedirs('Plots/OLR_Maps',exist_ok=True)

times=[]
for minute in range(0,5*10*12,5):
    times.append(datetime.datetime(2013,6,19,16,0,0)+datetime.timedelta(minutes=minute))

vmin=100
vmax=300
axes_extent=[-96.3,-93.9,28.4,30.5]

print('start plotting')
for case in cases:
    os.makedirs(os.path.join('Plots','OLR_Maps_5min',case,'All'),exist_ok=True)
    for time in times:
        print('start plotting ', time)

        constraint_time=iris.Constraint(time=time)
        fig3,ax3=plt.subplots(nrows=2,ncols=3,figsize=(30/2.54,20/2.54),squeeze=False,subplot_kw={'projection': ccrs.PlateCarree()})
        ax3_flat=ax3.flatten()
        for i,model in enumerate(models):
            print('start plotting ', model)

            fig4,ax4=plt.subplots(nrows=1,ncols=1,figsize=(10/2.54,10/2.54),subplot_kw={'projection': ccrs.PlateCarree()})
            os.makedirs(os.path.join('Plots','OLR_Maps_5min',case,model),exist_ok=True)
            OLR_i=OLR[case][model].extract(constraint_time)
            if OLR_i is not None:
                plot_OLR_subplot=plot_2D_map(OLR_i,title=model,axes_extent=axes_extent,axes=ax3_flat[i],vmin=vmin,vmax=vmax,n_levels=50,colormap=False,cmap='Blues')
                plot_2D_map(OLR_i,title=model,axes_extent=axes_extent,axes=ax4,vmin=vmin,vmax=vmax,n_levels=50,colormap=True,cmap='Blues')
                fig4.savefig(os.path.join('Plots','OLR_Maps_5min',case,model,'OLR_'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
            plt.close(fig4)
        fig3.colorbar(plot_OLR_subplot,orientation='horizontal',ax=ax4.ravel().tolist(), shrink=0.75)
        fig3.savefig(os.path.join('Plots','OLR_Maps_5min',case,'OLR_'+time.strftime('%Y-%m-%d %H:%M:%S')+'.png'),dpi=600)
        plt.close(fig3)
print('done')
