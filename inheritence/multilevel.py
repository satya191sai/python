class Parentcls1:
    def Function(self):
        self.a=30
        print("this is sai kumar")
class Parentcls2(Parentcls1):
    def FunctionName(self):
     print("this is child class")
class Childcls(Parentcls2):
     def Fu(self):
       print("this is grand child")     
             
obj=Childcls();
obj.Function()
obj.FunctionName()
obj.Fu()