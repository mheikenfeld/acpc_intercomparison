# Editted by PJM 2018 03 18
# Added time conversion to match RAMS/WRF models
# Added if statement for 2D or 3D variables

import iris
import numpy as np
from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag

import cf_units as unit
import datetime

def load_COSMO(files,variable):        
    
    # Test files / variables for PJM
    #files = '/avalanche/pmarin/ACPC/YELLOWSTONE/NOBAK/COSMO_C/lfff00100000.nc_5min'
    #variable = 'TOT_PREC'
    
    #files = files_CLN_500m_5min['COSMO_KIT']
    #variable = "precipitation_amount"

#    files = files_CLN_500m_5min['COSMO_KIT']
#    variable = 'net_downward_longwave_flux_in_air'


#    cube_test=iris.load(files[0],variable)

#
#    if variable == 'net_downward_longwave_flux_in_air':
#        cubes=iris.load(files,variable)
#        cubes2 = []
#        for i in np.arange(0,len(cubes),2):
#            cubes2.append(cubes[i])
#            
#        cubes = cubes[np.arange(0,len(cubes),2)]
#        cubes = cubes2        
#    
#    else:
#        cubes=iris.load(files,variable)

    variable_constraint = iris.Constraint(cube_func=(lambda c: c.var_name == variable))
    cubes=iris.load(files,variable_constraint)
    # cubes=iris.load(files,variable)

    for cube in cubes:
        cube.attributes=[]
        cube.coord('time').bounds=None      

        # Convert COSMO Time (Seconds after 2013-06-19 12:00:00) to Days after 1970-01-01 (which is in ramscube and wrfcube)
        datetime_init = datetime.datetime(2013,6,19,12,0,0)
        dt = datetime.timedelta(seconds=cube.coord('time').points[0])
        datetime_now = datetime_init+dt
        datetime_greg = ( (datetime_now - datetime.datetime(1970,1,1,0,0,0)).days + (datetime_now - datetime.datetime(1970,1,1,0,0,0)).seconds / 86400)

        cube.remove_coord('time')
        cube.add_dim_coord(iris.coords.DimCoord(np.array(datetime_greg),standard_name='time', long_name='time', var_name='time', 
                                                 units=unit.Unit('days since 1970-01-01', calendar='gregorian'), bounds=None, 
                                                 attributes=None, coord_system=None, circular=False),data_dim=0)    
        
    cubes = iris.cube.CubeList(cubes)
    cube_out=cubes.concatenate_cube('time')

    # for 3D variables (x,y,z)  
    if len(np.shape(cube_out)) == 4:
        model_level_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1]),standard_name="model_level_number")
        cube_out.add_dim_coord(model_level_coord,data_dim=1)
    
        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="x")
        cube_out.add_aux_coord(x_coord,data_dims=2)
    
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[3]),long_name="y")
        cube_out.add_aux_coord(y_coord,data_dims=3)
        
        if 'model_level_number' in [coord.name() for coord in cube_out.coords()]:
            if cube_out.coord('model_level_number').shape[0]==95:
                cube_out.add_aux_coord(geopotential_height_coord_stag,data_dims=cube_out.coord_dims('model_level_number'))
            if cube_out.coord('model_level_number').shape[0]==94:
                cube_out.add_aux_coord(geopotential_height_coord,data_dims=cube_out.coord_dims('model_level_number'))

    # for 2D variables (x,y)
    elif len(np.shape(cube_out)) == 3:

        x_coord=iris.coords.DimCoord(np.arange(cube_out.shape[1]),long_name="x")
        cube_out.add_aux_coord(x_coord,data_dims=1)
    
        y_coord=iris.coords.DimCoord(np.arange(cube_out.shape[2]),long_name="y")
        cube_out.add_aux_coord(y_coord,data_dims=2)
        
    return cube_out

