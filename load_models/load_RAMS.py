from ramscube import load
def load_RAMS(filenames,variable):
    cube_out=load(filenames,variable,add_coordinates='xy')
    return cube_out                    
