
# <-----no use ------->
import pandas
file = pandas.read_csv("database.csv",low_memory=False)
virus_md5=[]
for i in file["md5"]:
    virus_md5.append(i[2:-1])



virus_signature = 'b8f76630a62c4f0fe708cdb06c5c844b'
if virus_signature in virus_md5:
    print("virus found")
else:
    print("not found")
