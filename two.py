#capitalize method
a = "art"
x=a.capitalize()
print(x)
#title 
a = "are u there"
x=a.title()
print(x)
#istitle
a = "Are U There"
x=a.istitle()
print(x)
#lower
a = "pYThon"
x=a.lower()
print(x)
#upper
a = "Python"
x = a.islower()
print(x)
#swapcase
a = "pythON@"
x = a.swapcase()
print(x)
#split
a = "development"
x = a.split('e',2)
print(x)
#join
a = "hi"
x = a.join("abcd")
print(x)
#replacemethod
a = "d3v3lopm3nt"
x = a.replace('3','  ',2)
print(x)
#count
d = "potato"
x=d.count('o')
print(x)

a  =[1,2,3,4,5]
def double (val):
    return val*2
res = list(map(double,a))
print(res)
#sep and end
print ("1","2","3" ,sep =" 5")
#end
for i in range(11):
    print(i,end="")


