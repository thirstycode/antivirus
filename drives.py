import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print (drives)
