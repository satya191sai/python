class Parentcls:
    def Function(self):
        self.a=30
        print("this is sai kumar")
class Childcls(Parentcls):
    def FunctionName(self):
     print("this is child class")
obj=Childcls();
obj.FunctionName()
obj.Function()