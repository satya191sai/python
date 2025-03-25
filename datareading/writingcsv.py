import csv,json

f=open('data.json','r')
f1=open("employees.csv", "w", newline="")

emp_data=json.load(f)
writer = csv.writer(f1)
for emp in emp_data:
    enam=writer.writerow([emp['ename']])  # Writing multiple rows
    eid=writer.writerow([emp['id']])  # Writing multiple rows
print("CSV file created successfully!")
f.close()
f1.close()