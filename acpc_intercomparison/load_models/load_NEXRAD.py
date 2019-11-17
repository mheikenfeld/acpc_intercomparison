def load_Nexrad(filenames,variable):
    import iris
    from iris.cube import CubeList
    from iris import coords
    from datetime import datetime,timedelta
    from os.path import basename
    cube_list=[]
    for filename in filenames:
        cube=iris.load_cube(filename,'variable')#'equivalent_reflectivity_factor'
        #time=iris.load_cube(filename,'time')
        timestring=basename(filename)[12:27]
        time_point=datetime.strptime("".join(timestring), "%Y%m%d_%H%M%S")
        time_days=(time_point - datetime(1970,1,1)).total_seconds() / timedelta(1).total_seconds()
        x=iris.load_cube(filename,'X-coordinate in Cartesian system')
        y=iris.load_cube(filename,'Y-coordinate in Cartesian system')
        z=iris.load_cube(filename,'Z-coordinate in Cartesian system')
        lat=iris.load_cube(filename,'Latitude grid')
        lon=iris.load_cube(filename,'Longitude grid')
        cube.remove_coord('time')
        cube.add_dim_coord(coords.DimCoord(time_days, standard_name=None, long_name='time', var_name='time', units='days since 1970-01-01', bounds=None, attributes=None, coord_system=None, circular=False),0)
        cube.add_dim_coord(coords.DimCoord(x.data, standard_name=None, long_name='x', var_name='x', units='m', bounds=None, attributes=None, coord_system=None, circular=False),2)
        cube.add_dim_coord(coords.DimCoord(y.data, standard_name=None, long_name='y', var_name='y', units='m', bounds=None, attributes=None, coord_system=None, circular=False),3)
        cube.add_dim_coord(coords.DimCoord(z.data, standard_name=None, long_name='z', var_name='z', units='m', bounds=None, attributes=None, coord_system=None, circular=False),1)
        cube.add_aux_coord(coords.AuxCoord(lat.data, standard_name='latitude', long_name='latitude', var_name='latitude', units='degrees', bounds=None, attributes=None, coord_system=None),(2,3))
        cube.add_aux_coord(coords.AuxCoord(lon.data, standard_name='longitude', long_name='longitude', var_name='longitude', units='degrees', bounds=None, attributes=None, coord_system=None),(2,3))
        cube_list.append(cube)
    for member in cube_list:
        member.attributes={}
    variable_cubes=CubeList(cube_list)
    variable_cube=variable_cubes.concatenate_cube()
    
    return variable_cube