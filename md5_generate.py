import hashlib
def md5(file_loc):
    try:
        hasher = hashlib.md5()
        with open(file_loc, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except PermissionError:
        pass
    except MemoryError:
        pass
