import csv,json

old_f=open("data.csv","r")
data = csv.reader(old_f)

# Write to a new JSON file
print(data)
print(type(data))
lists=list(data)
for user in lists:
 print(user[1:3])
