"""s=[]
tos=-1
def push(a):
    global tos
    tos+=1
    s.insert(tos,a)
    return s
def pop():
    global tos
    p=""
    if(tos<=1):
        print("Stack is empty")
        return -1
    else:
        p=s.pop(tos)
        tos-=1
        return p
def top():
    t=""
    t=s[len(s)-1]
    return t
def empty():
    return(tos<=-1)
print(type(empty()))
precedence={
    '/':3,
    '*':3,
    '+':2,
    '-':2,
    '(':-1,
    ')':-1,
    }
x=str(input("Enter the expression"))
st=""
for i in range(0,len(x)):
    if(x[i]=='0' or x[i]=='1' or x[i]=='2'  or x[i]=='3' or x[i]=='4' or x[i]=='5' or x[i]=='6' or x[i]=='7' or x[i]=='8' or x[i]=='9'):
        st="""
infix=str(input("Enter the expression"))
prior={'+':1,'-':1,'/':2,'*':2,'^':3}
def convert(infix):
    stk=[]
    post=[]
    for i in infix:
        if(i.isdigit()):
            post.append(i)
        elif(i=='('):
            stk.append(i)
        elif(i==')'):
            while(stk[-1]!='('):
                post.append(stk.pop())
                stk.pop()
        else:
            while(stk and stk[-1]!='(' and prior[i]<=prior[stk[-1]]):
                post.append(stk.pop())
                stk.append(i)
            while(stk!=[]):
               post.append(stk.pop())
    return post
print(convert(infix))
















        
