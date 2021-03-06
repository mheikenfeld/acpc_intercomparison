from wrfcube import load
from .make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag
from cf_units import Unit


def load_WRF(files,variable):
    from iris.cube import CubeList
    #check is variable is list or str and then either load single cube or cubelisr
    if type(variable)==list:
        output=CubeList()
        for variable_i in variable:
            output.append(load_WRF_cube(files,variable_i))
    elif type(variable)==str:
        output=load_WRF_cube(files,variable)
    return output

def load_WRF_cube(filenames,variable):

    cube_out=load(filenames,variable,add_coordinates='xy')    
    cube_out.coord('time').units = Unit(cube_out.coord('time').units.origin, calendar='gregorian')  
    
    new_time_unit = Unit('days since 1970-01-01', calendar='gregorian')
    cube_out.coord('time').convert_units(new_time_unit)

    if 'model_level_number' in [coord.name() for coord in cube_out.coords()]:
        if cube_out.coord('model_level_number').shape[0]==95:
            cube_out.add_aux_coord(geopotential_height_coord_stag,data_dims=cube_out.coord_dims('model_level_number'))
        if cube_out.coord('model_level_number').shape[0]==94:
            cube_out.add_aux_coord(geopotential_height_coord,data_dims=cube_out.coord_dims('model_level_number'))


    return cube_out
