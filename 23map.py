# numbers = ["3","34","64"]
# numbers = list(map(int,numbers))

# # for i in range (len(numbers)):
# #     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2]+1
# print(numbers[2])


# **************************************************

# # def sq(a):
# #     return a*a

# num = [2,3,5,6,3,1,12]
# # square = list(map(sq,num))
# square = list(map(lambda a: a*a,num))
# print(square)


# ****************************************************

def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square,cube]

for i in range(5):
    val= list(map(lambda x:x(i),func))
    print(val)