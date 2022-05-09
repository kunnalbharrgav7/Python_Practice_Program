# print("enter your first number : ")
num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
operater = input("enter your operation +,-,/,* ")

if (num1==45 and num2 == 3 or num1 == 3 and num2 == 45) and operater == '*':
    print(num1,operater,num2 ,"= 7777")
    
elif (num1==56 and num2 == 9 or num1 == 9 and num2 == 56) and operater == '+':
    print(num1,operater,num2 ,"= 676")
    
elif (num1==56 and num2 == 6 or num1 == 6 and num2 == 56) and operater == '/':
    print(num1,operater,num2 ,"= 43")
    
else:
    if (operater == '+'):
        print(num1,operater,num2 ," = ",num1+num2)
    elif (operater == '-'):
        print(num1,operater,num2 ," = ",num1-num2)
    elif (operater == '*'):
        print(num1,operater,num2 ," = ",num1*num2)
    elif (operater == '/'):
        print(num1,operater,num2 ," = ",num1/num2)
        
