""" Take user defined values.And ask user to perform a particular arithmatic operation.
Output like(3-1=2)
Using functions.
"""
def add(a,b):
    return a+b
def  sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def power(a,b):
    return a**b
def sqr(a):
    return a**a
def cube(a):
    return a**3
def sqrt(a):
    return a**(1/2)
def cbrt(a):
    return a**(1/3)

print("Welcome to my calculator")

print("Select choice")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Power")
print("7.Square")
print("8.cube")
print("9.Square root")
print("10.Cube root")
choice=input("1/2/3/4/5/6/7/8/9/10")

print("Which type of number do you want to perform opertation.\nEnter 1 for integer type and 2 for float type")
num=input("1/2")
if choice=="7/8/9/10":
    if num==1:
        a=float(input("Enter the first number"))
    else:
        a=float(input("Enter the first number"))
        b=float(input("Enter the second number"))
    
elif choice=="7/8/9/10":
    a=int(input("Enter the first number"))
else:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
        
if choice=="1":
    print(a,"+",b,"=",add(a,b))
elif choice=="2":
    print(a,"-",b,"=",sub(a,b))
elif choice=="3":
    print(a,"*",b,"=",mul(a,b))
elif choice=="4":
    print(a,"/",b,"=",div(a,b))
elif choice=="5":
    print(a,"%",b,"=",mod(a,b))
elif choice=="6":
    print(a,"power",b,"=",power(a,b))
elif choice=="7":
    print(a,"square = ",sqr(a))
elif choice=="8":
    print(a,"cube =",cube(a))
elif choice=="9":
    print(a,"square root =",sqrt(a))
elif choice=="10":
    print(a,"cube root =",cbrt(a))






    
