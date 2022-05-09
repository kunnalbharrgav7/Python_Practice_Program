a=int(input("Enter number a"))
b=int(input("Enter number b"))
c=int(input("Enter number c"))

if a>b and a>c:
    print(a," is greater than",b ,"and",c)
elif b>a and b>c:
    print(b," is greater than",c ,"and",a)
elif c>a and c>b:
    print(c," is greater than",a ,"and",b)
elif a==b and a>c and b>c:
    print("a and b are greater than c")
elif b==c and b>a and c>a:
    print("b and c are greater than a")
elif a==c and a>b and c>b:
    print("a and c are greater than b")    
    
else:
    print("All Values are equal")

#write a python script to find greatest number in n inputs.
#To make a excel sheet for marks in three internals and take best of two.    
