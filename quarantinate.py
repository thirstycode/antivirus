import os
import socket
def delete(root,filename,threats_cleaned):

    if os.path.isfile(filename):
        os.remove(filename)
        print(" %s is Deleted"% filename)
        ++threats_cleaned
    else:
        print("Error: %s is not Deleted" % filename)
