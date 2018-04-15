# <----NO Use in orignal code------>


# ---TO get list of drives in hardrive---
import win32api


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print (drives)
