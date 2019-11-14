from ramscube import load
from cf_units import Unit

def load_RAMS(files,variable):
    from iris.cube import CubeList
    #check is variable is list or str and then either load single cube or cubelisr
    if type(variable)==list:
        output=CubeList()
        for variable_i in variable:
            output.append(load_RAMS_cube(files,variable_i))
    elif type(variable)==str:
        output=load_RAMS_cube(files,variable)
    return output


def load_RAMS_cube(filenames,variable):
    cube_out=load(filenames,variable,add_coordinates='xy')
    new_time_unit = Unit('days since 1970-01-01', calendar='gregorian')
    cube_out.coord('time').convert_units(new_time_unit)

    return cube_out                    
