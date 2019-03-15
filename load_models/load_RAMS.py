from ramscube import load
from cf_units import Unit
def load_RAMS(filenames,variable):
    cube_out=load(filenames,variable,add_coordinates='xy')
    new_time_unit = Unit('days since 1970-01-01', calendar='gregorian')
    cube_out.coord('time').convert_units(new_time_unit)

    return cube_out                    
