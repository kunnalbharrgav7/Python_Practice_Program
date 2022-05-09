import time
begin=time.time()
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact(x-1)
        return y
"""val=int(input("Enter the number"))
funct_val=fact(val)
print("Factorial of {} is {}".format(val,funct_val))"""
for i in range(5,996):
    funct=fact(i)
    print(funct)
end=time.time()

begin1=time.time()
for i in range(5,996):
    fact=i*(i-1)
    print(fact)
end1=time.time()
print("time=",end-begin)
print("time 2 =",end1-begin1 )
