import json
emp='''{"eid":101,"esal":true,"ename":"sai"}'''
emp_dict=json.loads(emp)
print(emp_dict)