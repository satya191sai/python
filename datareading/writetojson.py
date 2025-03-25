import json
 
f=open('employees.csv','w')
f1=json.dump(f)
print(f1)
f.close()

