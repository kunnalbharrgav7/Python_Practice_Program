def avg(* value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=avg(3,4,5)
print(y)
y=avg(12,34,55,33,22,11)
print(y)
