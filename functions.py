'''def sample(a,b):
    print(a+b)
a=int(input())
b=int(input())
sample(a,b)
a=123
b=123
sample(a,b)'''
def sample(a,b):#formal parameters
    return (a+b)
def add(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a//b)
'''
a,b=map(int,input().split())
c=int(input())
if c==1:
    add(a,b)
elif c==2:
    sample(a,b)
elif c==3:
    mul(a,b)#actual parameters
else:
    div(a,b)'''
#group of functions together called a module this the reason python is easy as they perform various functions





