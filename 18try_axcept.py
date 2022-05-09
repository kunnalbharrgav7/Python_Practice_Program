a=input("enter first number ")
b=input("enter second number ")
# print("the sum of two numbers are : ",a+b)

try:
    print("the sum of these two numbers is ",
          int(a)+int(b))
    
except Exception as e:
    print(e)

finally:    
    print("This is finally statment ")



# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print("The sum of these two numbers is",
#           int(num1)+int(num2))
# except Exception as e:
#     print(e)



# print("This line is very important")