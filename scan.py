import os
import pandas
import md5_generate
import status

folders_scanned=1
files_scanned=0
threats_detected = 0
threats_cleaned = 0

file = pandas.read_csv("database.csv",low_memory=False)
virus_md5=[]
for i in file["md5"]:
    virus_md5.append(i[2:-1])

for root, directories, filenames in os.walk('D://softwares'):
     for directory in directories:
         folders_scanned += 1
         # print( os.path.join(root, directory))
     for filename in filenames:
         files_scanned += 1
         md5_key = md5_generate.md5(os.path.join(root,filename))
         if md5_key in virus_md5:
             threats_detected += 1
             # <------TODo Quarantinate Function ------------->
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
