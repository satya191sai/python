import json
fp1 = open('data.json','r')
emp_data=json.load(fp1)
print(type(emp_data))

for emp in emp_data:
    print(emp['ename'])