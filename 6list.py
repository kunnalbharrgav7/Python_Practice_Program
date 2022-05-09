# grocery = ["tomato","papaya","apple","ladyfinger","potato",324453565667]
# print("1",grocery)
# print("2",grocery[3])
# #print("3",grocery[6])error

# print("*********************************************************************")

number = ["23","25","87","65","89","56"]
print("1",number)

number.sort()
print("2",number)

number.reverse()
print("3",number)
print("4",number[2])
print("5",number[1:4])
print("6",len(number))
print("7",max(number))
print("8",min(number))
number.append(7)#end m "7" add kr dega 
print("9",number)

b=[223,56,7,89,45,12,54]
print("1",b)
 
b.append(420)
print("2",b)

b.insert(2,67)#mtlb 2nd index pr 67 add ho jayega puri list aage bd jayegi
print("3",b)

b.remove(7)
print("4",b)

b.pop()
print("5",b)#last baala number ht jayega list m se

b[1]=6  #ye 1st index pr 67 layega remove krke
print("6",b)


# # print("**********************************************************************")
# # ise tpple kehte h ye list se alg hota h 
# r=(1,2,3,4,5,6,7,8)
# print(r)





l = []
n=int(input())
for i in range(0,n):
    m=int(input())
    l.append(m)

l.sort()
if l[-1] == l[-2]:
    print(l[-3])
elif l[-1] != l[-2]:
    print(l[-2])