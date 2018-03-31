from ramscube import loadramscube
def load_RAMS(filenames,variable):
    cube_out=loadramscube(filenames,variable,add_coordinates='xy')
    return cube_out                    
