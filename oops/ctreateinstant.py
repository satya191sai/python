class employee:
    orgn='tcs'
    def __init__(self):
        self.eid=20
    def Fun(self):
        self.e=30          
a=employee()
a1=employee()
a1.Fun()
del a1.e
print(a1.__dict__)
print(a.__dict__)
print(employee.__dict__)