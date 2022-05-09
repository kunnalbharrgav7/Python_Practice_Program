a=input("enter a string : ")
b="the length of our string is "
l=len(a)
#print("the length of our string is ",l)
print("the length of our string is "+str(l))
#print("the length of our string is "+l)   #TypeError: can only concatenate str (not "int") to str
#print("length of string ={}".format(l))
#print(b,l)
for i in range(l):
    print(a[i],": is at index :",i)
