from sqlite3 import Time
from time import *
n = int(input("Enter first number : "))
m = int(input("Enter second number : "))
o = int(input("Enter third number : "))
start_time = time()
print(start_time)
num = max(m, n, o)
while num <= n*m*o:
    if num % n == 0 and num % m == 0 and num % o == 0:
        break
    num += 1

print("LCM is ", num)
end_time = time()
print(end_time)
print(end_time-start_time)
