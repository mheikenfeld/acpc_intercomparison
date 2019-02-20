from wrfcube import load
from load_models.make_geopotential_height_coord import geopotential_height_coord,geopotential_height_coord_stag

def load_WRF(filenames,variable):
    cube_out=load(filenames,variable,add_coordinates='xy')
#    latitude_coord=cube_out.coord('latitude').copy(points=cube_out.coord('latitude').points[0])
#    longitude_coord=cube_out.coord('longitude').copy(points=cube_out.coord('longitude').points[0])
#    cube_out.remove_coord('latitude')
#    cube_out.remove_coord('longitude')
#    cube_out.add_aux_coord(latitude_coord,data_dims=(cube_out.coord_dims('south_north')[0],cube_out.coord_dims('west_east')[0]))
#    cube_out.add_aux_coord(longitude_coord,data_dims=(cube_out.coord_dims('south_north')[0],cube_out.coord_dims('west_east')[0]))
    if 'model_level_number' in [coord.name() for coord in cube_out.coords()]:
        if cube_out.coord('model_level_number').shape[0]==95:
            cube_out.add_aux_coord(geopotential_height_coord_stag,data_dims=cube_out.coord_dims('model_level_number'))
        if cube_out.coord('model_level_number').shape[0]==94:
            cube_out.add_aux_coord(geopotential_height_coord,data_dims=cube_out.coord_dims('model_level_number'))

    return cube_out
