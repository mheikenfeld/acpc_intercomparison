# Created based on file for loading the UM, MH 2019-02-26
# Added time conversion to match RAMS/WRF models
# Added if statement for 2D or 3D variables

import iris
import os
import numpy as np
from copy import deepcopy
from cf_units import Unit
def load_concatentate(files,variable):
    cubes=iris.load(files,variable)
    for cube in cubes:
        cube.attributes=[]
        cube.coord('time').bounds=None
    cube_out=cubes.concatenate_cube('time')
    return cube_out

def load_MesoNH(files,variable):
    from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag
    cubes=iris.load(files)
    #Z=iris.load_cube(files,'Z')
    lat=iris.load_cube(files[0],'lat')
    lon=iris.load_cube(files[0],'lon')
    
    cube_out=load_concatentate(files,variable)
    
    new_time_unit = Unit('days since 1970-01-01', calendar='gregorian')
    cube_out.coord('time').convert_units(new_time_unit)

    # for 4D variables (time,z,y,x)
    if len(np.shape(cube_out)) == 4:
    
        model_level_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1]),standard_name="model_level_number")
        cube_out.add_dim_coord(model_level_coord,data_dim=1)
    
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="y")
        cube_out.add_dim_coord(y_coord,data_dim=2)
        
        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[3]),long_name="x")
        cube_out.add_dim_coord(x_coord,data_dim=3)

        lon_coord=iris.coords.AuxCoord(lon.data,standard_name="longitude")
        cube_out.add_aux_coord(lon_coord,data_dims=(2,3))
    
        lat_coord=iris.coords.AuxCoord(lat.data,standard_name="latitude")
        cube_out.add_aux_coord(lat_coord,data_dims=(2,3))
    
        #Z_coord=iris.coords.AuxCoord(Z[0].core_data(),standard_name="geopotential_height")
        #cube.add_aux_coord(Z_coord,data_dims=(1,2,3))
        if 'model_level_number' in [coord.name() for coord in cube_out.coords()]:
            if cube_out.coord('model_level_number').shape[0]==95:
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord_stag),data_dims=cube_out.coord_dims('model_level_number'))
                
            if cube_out.coord('model_level_number').shape[0]==94:
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord),data_dims=cube_out.coord_dims('model_level_number'))

    # for 3D variables (time,x,y)
    elif len(np.shape(cube_out)) == 3:
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1]),long_name="y")
        cube_out.add_dim_coord(y_coord,data_dim=1)

        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="x")
        cube_out.add_dim_coord(x_coord,data_dim=2)
    
        lon_coord=iris.coords.AuxCoord(lon.data,standard_name="longitude")
        cube_out.add_aux_coord(lon_coord,data_dims=(1,2))
    
        lat_coord=iris.coords.AuxCoord(lat.data,standard_name="latitude")
        cube_out.add_aux_coord(lat_coord,data_dims=(1,2))

    return cube_out


