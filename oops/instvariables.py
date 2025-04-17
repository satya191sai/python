class employee:
    orgn='tcs'
    def __init__(self,id,name,sal):
        self.eid=id
        self.ename=name
        self.esal=sal
    def Fun(cls):
        cls.e=30  
        
a=employee(101,'satya',430000)
a1=employee(102,'sai',550000)
a2=employee(103,'roopa',660000)
a.Fun()
print(a.__dict__)
print(a1.__dict__)
print(a2.__dict__)
print(employee.__dict__)
        