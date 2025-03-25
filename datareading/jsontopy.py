import json
 
f=open('data.json','r')
emp_data=json.load(f)
print(emp_data)
for emp in emp_data:
    print(emp['id'])