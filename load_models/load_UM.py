# Editted by PJM 2018 03 18
# Added time conversion to match RAMS/WRF models
# Added if statement for 2D or 3D variables

import iris
import os
import numpy as np
import datetime
from cf_units import date2num,CALENDAR_STANDARD
from copy import deepcopy
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
    from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag

#    model = 'UM_LEEDS'
#    files = files_CLN_500m_5min[model]
#    variable = variable_names[model]['OLR']
    # files=files[1:] # Bad first file in UM data -- getting the following error
####iris.exceptions.ConcatenateError: failed to concatenate into a single cube.
#  An unexpected problem prevented concatenation.
    #    Test Files
    #    files = '/avalanche/pmarin/ACPC/YELLOWSTONE/NOBAK/UM_C/*20130619_21*.nc'
    #    variable = 'pcp_accum'


    filename_aux=os.path.join(os.path.dirname(files[0]),'LMCONSTANTS')
    Z=iris.load_cube(filename_aux,'Z')
    lat=iris.load_cube(filename_aux,'lat')
    lon=iris.load_cube(filename_aux,'lon')
    
    cubes=iris.load(files,variable,callback=callback)
    for cube in cubes:
        cube.attributes=[]
        cube.coord('time').bounds=None

#         # Convert UM Time (Seconds after 2013-06-19 16:00:00) for 5 minute data  to Days after 1970-01-01 (which is in ramscube and wrfcube)
# 	# Convert UM Time (Seconds after 2013-06-19 12:00:00) for hourly data       
#         datetime_init = datetime.datetime(2013,6,19,12,0,0)
#         dt = datetime.timedelta(seconds=np.float64(cube.coord('time').points[0]))
#         datetime_now = datetime_init+dt
#         datetime_greg = ( (datetime_now - datetime.datetime(1970,1,1,0,0,0)).days + (datetime_now - datetime.datetime(1970,1,1,0,0,0)).seconds / 86400)

#         cube.remove_coord('time')
#         cube.add_dim_coord(iris.coords.DimCoord(np.array(datetime_greg),standard_name='time', long_name='time', var_name='time', 
#                                                  units=unit.Unit('days since 1970-01-01', calendar='gregorian'), bounds=None, 
#                                                  attributes=None, coord_system=None, circular=False),data_dim=0)    

    cube_out=cubes.concatenate_cube('time')

    # for 3D variables (x,y,z)
    if len(np.shape(cube_out)) == 4:
    
        model_level_coord=iris.coords.DimCoord(np.arange(Z.shape[1],0,-1),standard_name="model_level_number")
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
                #cosmo has top to bottom levels, flip around coordinates
                cube_out.add_aux_coord(deepcopy(geopotential_height_coord),data_dims=cube_out.coord_dims('model_level_number'))
            #the UM has top to bottom levels, flip around coordinates

            coord=cube_out.coord('geopotential_height').points
            cube_out.coord('geopotential_height').points=np.flip(coord,axis=0)

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


