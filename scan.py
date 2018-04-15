import os
import pandas
import win32api
import md5_generate
import status
import quarantinate

folders_scanned=1
files_scanned=0
threats_detected = 0
threats_cleaned = 0

file = pandas.read_csv("database_md5.csv",low_memory=False)
virus_md5 = file["md5"].tolist()
file2 = pandas.read_csv("database_name.csv",low_memory=False)
virus_name = file2["name"]

select = input("Antivirus\n[a] Start Scan\n[b] See Scan Log\n[x] Exit\nSelection: ")
if select == "a":
    select1 = input("Choice\n[a] Full Scan\n[b] Custom Scan\nSelection: ")
    if select1 == "a":
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
    elif select == "b":
        drives = [raw_input("Enter Location To Be Scanned : ")]
    else:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]

    for i in drives:
        for root, directories, filenames in os.walk(i):
             for directory in directories:
                 folders_scanned += 1
                 # print( os.path.join(root, directory))
             for filename in filenames:
                 files_scanned += 1
                 md5_key = md5_generate.md5(os.path.join(root,filename))
                 if md5_key in virus_md5:
                     threats_detected += 1
                     # <------TODo Quarantinate Function ------------->
                     threats_cleaned = quarantinate.delete(os.path.join(root,filename),threats_cleaned)
                 else:
                     pass
                    # print("virus not found")
                 # print("Total Files Scanned : " + str(files_scanned))
                 # print (os.path.join(root,filename))
                 status.current_scan(os.path.join(root,filename))
                 status.status_scan(files_scanned,folders_scanned,threats_detected,threats_cleaned)

    print("Scanning Completed ...!")
    # TODo Save Log
    print("Details Saved ...!")

elif select == "b":
    # <--------Todo----->
    pass

elif select == "x":
    sys.exit(0)

else:
	print("Incorrect selection")
