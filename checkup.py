
# <-----no use ------->
import pandas
file = pandas.read_csv("database_total.csv",low_memory=False)
virus_md5 = str(file["md5"])
virus_name = str(file["name"])

# print(virus_name)
print(virus_name[10])
virus_signature = '047395207d2e40681592be7f7b33c49e'
if virus_signature in virus_md5:
    print("virus found")
    print(virus_md5.index(virus_signature))
    print(virus_name[int(virus_md5.index(virus_signature))])
else:
    print("not found")
