class Grandparentcls1:
    def Function(self):
        self.a=30
        print("this is grand parent ")
class Parentcls1(Grandparentcls1):
    def FunctionName(self):
     print("this is parent1")
class Parentcls2(Grandparentcls1):
     def Fu(self):
       print("this is parent2") 
class Childcls2(Parentcls2,Parentcls1):           
     def Fun(self):
       print("this is hibride ")     
         
obj=Childcls2();
obj.Function()
obj.FunctionName()
obj.Fu()
obj.Fun()