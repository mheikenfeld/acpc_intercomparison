# Editted by PJM 2018 03 18
# Added time conversion to match RAMS/WRF models
# Added if statement for 2D or 3D variables

import iris
import os
import numpy as np
import datetime
from cf_units import date2num,CALENDAR_STANDARD
from copy import deepcopy
from dask.array import cumsum
def callback(cube, field, filename):
    from re import sub
    if '.nc' in filename:
        timeobj = datetime.datetime.strptime(sub("\D", "", os.path.basename(filename)),"%Y%m%d%H%M")
        base_date=datetime.datetime(1970,1,1)
        time_units='days since '+ base_date.strftime('%Y-%m-%d')
        time_days=date2num(timeobj, time_units, CALENDAR_STANDARD)
        cube.coord('time').points=time_days
        cube.coord('time').units=time_units
    return cube

def load_UM(files,variable):
    from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag,geopotential_height_coord_short

    filename_aux=os.path.join(os.path.dirname(files[0]),'LMCONSTANTS')
    #Z=iris.load_cube(filename_aux,'Z')
    lat=iris.load_cube(filename_aux,'lat')
    lon=iris.load_cube(filename_aux,'lon')
    
    cubes=iris.load(files,variable,callback=callback)
    for cube in cubes:
        cube.attributes=[]
        cube.coord('time').bounds=None

    cube_out=cubes.concatenate_cube('time')

    # for 3D variables (x,y,z)
    print(len(cube_out.shape))
    if len(cube_out.shape) == 4:
    
        model_level_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1],0,-1),standard_name="model_level_number")
        cube_out.add_dim_coord(model_level_coord,data_dim=1)
    
        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="y")
        cube_out.add_dim_coord(x_coord,data_dim=2)
    
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[3]),long_name="x")
        cube_out.add_dim_coord(y_coord,data_dim=3)
    
        if (cube_out.shape[2]==lat.shape[1] and cube_out.shape[3]==lat.shape[2]):
            lon_coord=iris.coords.AuxCoord(lon[0].data,standard_name="longitude")
            cube_out.add_aux_coord(lon_coord,data_dims=(2,3))

            lat_coord=iris.coords.AuxCoord(lat[0].data,standard_name="latitude")
            cube_out.add_aux_coord(lat_coord,data_dims=(2,3))
    
        #Z_coord=iris.coords.AuxCoord(Z[0].core_data(),standard_name="geopotential_height")
        #cube.add_aux_coord(Z_coord,data_dims=(1,2,3))
        if 'model_level_number' in [coord.name() for coord in cube_out.coords()]:
            
            if cube_out.coord('model_level_number').shape[0]==95:
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord_stag),data_dims=cube_out.coord_dims('model_level_number'))
                
            if cube_out.coord('model_level_number').shape[0]==94:
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord),data_dims=cube_out.coord_dims('model_level_number'))
            
            if cube_out.coord('model_level_number').shape[0]==93:
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord_short),data_dims=cube_out.coord_dims('model_level_number')) 
                
            #the UM has top to bottom levels, flip around coordinates
            coord=cube_out.coord('geopotential_height').points
            cube_out.coord('geopotential_height').points=np.flip(coord,axis=0)

    # for 2D variables (x,y)
    elif len(np.shape(cube_out)) == 3:

        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1]),long_name="y")
        cube_out.add_dim_coord(x_coord,data_dim=1)
    
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="x")
        cube_out.add_dim_coord(y_coord,data_dim=2)
        
        if (cube_out.shape[1]==lat.shape[1] and cube_out.shape[2]==lat.shape[2]):
            lon_coord=iris.coords.AuxCoord(lon[0].core_data(),standard_name="longitude")
            cube_out.add_aux_coord(lon_coord,data_dims=(1,2))

            lat_coord=iris.coords.AuxCoord(lat[0].core_data(),standard_name="latitude")
            cube_out.add_aux_coord(lat_coord,data_dims=(1,2))
        
    #create accumulated precip variable as for other models:
    if variable=='pcp_accum':
        cube_out.data = cumsum(cube_out.core_data(), axis=0); # Make Cumulative Sum

    return cube_out


