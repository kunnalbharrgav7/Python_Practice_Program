a=int(input("Enter the year to know wheather its leap or not"))
while(a%4==0):
    if(a%100==0):
        print("Its not a leap year")
    elif(a%400==0 and a%100==0):
        print("It is a leap year") 
        
    
