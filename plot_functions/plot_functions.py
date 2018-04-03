import matplotlib.pyplot as plt

def plot_2D_map(cube_in,axes_extent=None,title=None,axes=plt.gca(),vmin=None,vmax=None,n_levels=50,cmap='viridis',colorbar=True,**kwargs):
    import cartopy
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    import iris.plot as iplt
    from matplotlib.ticker import MaxNLocator
    import cartopy.feature as cfeature
    import numpy as np
    from matplotlib import ticker
    
    if type(axes) is not cartopy.mpl.geoaxes.GeoAxesSubplot:
        raise ValueError('axes had to be cartopy.mpl.geoaxes.GeoAxesSubplot')

    
    datestring=cube_in.coord('time').units.num2date(cube_in.coord('time').points[0]).strftime('%Y-%m-%d %H:%M:%S')

    axes.set_title(str(title)+'    ' + datestring,fontsize=8)
    
    gl = axes.gridlines(draw_labels=True)
    majorLocator = MaxNLocator(nbins=5,steps=[1,2,5,10])
    gl.xlocator=majorLocator
    gl.ylocator=majorLocator
    gl.xformatter = LONGITUDE_FORMATTER
    axes.tick_params(axis='both', which='major', labelsize=6)
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabels_top = False
    gl.ylabels_right = False
    axes.coastlines('10m')    
    #    rivers=cfeature.NaturalEarthFeature(category='physical', name='rivers_lake_centerlines',scale='10m',facecolor='none')
    lakes=cfeature.NaturalEarthFeature(category='physical', name='lakes',scale='10m',facecolor='none')
    axes.add_feature(lakes, edgecolor='black')
    axes.set_xlabel('longitude')
    axes.set_ylabel('latitude')  


    axes.set_extent(axes_extent)
    
    plot_cube=iplt.contourf(cube_in,coords=['longitude','latitude'],
                        levels=np.linspace(vmin,vmax,num=n_levels),axes=axes,cmap=cmap,vmin=vmin,vmax=vmax,extend='both',**kwargs)
    
    if colorbar==True:
        cbar=plt.colorbar(plot_cube,orientation='vertical',ax=axes)
        cbar.ax.set_xlabel(cube_in.name()+ '(' + cube_in.units.symbol +')') 
        tick_locator = ticker.MaxNLocator(nbins=5)
        cbar.locator = tick_locator
        cbar.update_ticks()
    
    return plot_cube

