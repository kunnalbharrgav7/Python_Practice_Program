import fact 
"""n=int(input("Enter the first number"))
r=int(input("Enter the second number"))
x=fact.fact(n)
y=fact.fact(n-r)
result=x/y
print(result)"""

n=int(input("Enter the first number"))
r=int(input("Enter the second number"))
r1=int(input("Enter the third number"))
x=fact.fact(n)
y=fact.fact(n-r)
z=fact.fact(r1)
result=x/y*z
print(result)

