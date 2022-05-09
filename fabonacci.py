def fab(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fab(n-1)+fab(n-2)
    
    
number=int(input("enter the number :"))
print(fab(number))

# 1 2 3 5 8 13