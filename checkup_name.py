
# <-----no use ------->
import pandas
file = pandas.read_csv("database_name.csv",low_memory=False)
virus_name = str(file["name"])

# print(virus_name)

# <------ye niche wali cheez print nahi hori---->  dekh to ekbar
print(virus_name[10])
