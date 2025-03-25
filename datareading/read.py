fp1=open("abc.txt",'r')
fp2=open('xyz.txt','w')

data=fp1.read()
fp2.write(data)
print("New file Created successfully")
fp1.close()
fp2.close()