# Editted by PJM 2018 03 18
# Added time conversion to match RAMS/WRF models
# Added if statement for 2D or 3D variables

import iris
import os
import numpy as np
from copy import deepcopy

def load_UM(files,variable):
    from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag

    Z=iris.load_cube(filename_aux,'Z')
    lat=iris.load_cube(filename_aux,'lat')
    lon=iris.load_cube(filename_aux,'lon')
    
    cubes=iris.load(files,variable)
    for cube in cubes:
        cube.attributes=[]
        cube.coord('time').bounds=None

    cube_out=cubes.concatenate_cube('time')

    # for 3D variables (x,y,z)
    if len(np.shape(cube_out)) == 4:
    
        model_level_coord=iris.coords.DimCoord(np.arange(Z.shape[1]),standard_name="model_level_number")
        cube_out.add_dim_coord(model_level_coord,data_dim=1)
    
        x_coord=iris.coords.DimCoord(np.arange(Z.shape[2]),long_name="x")
        cube_out.add_dim_coord(x_coord,data_dim=2)
    
        y_coord=iris.coords.DimCoord(np.arange(Z.shape[3]),long_name="y")
        cube_out.add_dim_coord(y_coord,data_dim=3)
    
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

    # for 2D variables (x,y)
    elif len(np.shape(cube_out)) == 3:

        x_coord=iris.coords.DimCoord(np.arange(Z.shape[2]),long_name="x")
        cube_out.add_dim_coord(x_coord,data_dim=1)
    
        y_coord=iris.coords.DimCoord(np.arange(Z.shape[3]),long_name="y")
        cube_out.add_dim_coord(y_coord,data_dim=2)
    
        lon_coord=iris.coords.AuxCoord(lon[0].data,standard_name="longitude")
        cube_out.add_aux_coord(lon_coord,data_dims=(1,2))
    
        lat_coord=iris.coords.AuxCoord(lat[0].data,standard_name="latitude")
        cube_out.add_aux_coord(lat_coord,data_dims=(1,2))

    return cube_out


