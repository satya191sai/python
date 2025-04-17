class variables:
    a=10
    def __init__(self):
        self.b=20
        self.e=30
    def c(self):
        self.d=40

v=variables()
v.c()
print(variables.__dict__)
print(v.__dict__)

