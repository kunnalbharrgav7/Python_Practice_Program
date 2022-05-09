"""
print("This script is intended to swap the values of two data variables using a third variable ")
a=int(input("enter the first integer : "))
b=int(input("enter the second integer : "))

print("before swapping ")
print("value of a and b is ",a,b)

temp = a
a = b
b = temp

print("after swapping ")
print("value of a and b is ",a,b)

"""

print("This script is intended to swap the values of two data variables using a third variable ")
a=(input("enter the first integer : "))
b=(input("enter the second integer : "))

print("before swapping ")
print("value of a and b is ",a,b)

a=int(a)
b=int(b)
"""
temp = a
a = b
b = temp
"""
"""
a=a+b
b=a-b
a=a-b
"""
a,b=b,a

print("after swapping ")
print("value of a and b is ",str(a),str(b))
