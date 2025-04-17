class Parentcls1:
    def Function(self):
        self.a=20
        print(self.a)
        print("this is sai kumar")
class Parentcls2:
    def Function(self):
     print("this is child class")
class Childcls(Parentcls1,Parentcls2):
     def Fu(self):
       print("this is grand child")     
             
obj=Childcls();
obj.Function()
obj.Fu()
print(obj.__dict__)
