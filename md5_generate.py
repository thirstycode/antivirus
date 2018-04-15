#<--------- generating md5 of a file from a file loaction ------------>
import hashlib
def md5(file_loc):
    try:
        hasher = hashlib.md5()
        with open(file_loc, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        return hasher.hexdigest()          #returns md5 key 
    
#    <---- Exceptions Below ----->
#    <---- Need To Add Fixing Module --->
    except PermissionError:
        pass
    except MemoryError:
        pass
