class test:
    org='tcs'
    def __init__(self):
        self.a=20
    def F1(cls):
        cls.b=30
        test.d=60
    def F2(self):
        self.c=40
t=test()
t1=test()
t.F1()
t.F2()
t1.F1()
t1.F2()
test.f=90
print(t.__dict__)
print(t1.__dict__)
print(test.__dict__)


        