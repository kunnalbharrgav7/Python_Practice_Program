def prime(x):
    for i in range (2,x):
        if x%i==0:
            return False
        else :
            return True

filtered=filter(prime,range(10))

print("prime numbers are : ",list(filtered))