'''import functions
a=int(input())
b=int(input())
#c=functions.add(a,b)
from functions import mul
c=mul(a,b)
print(c)'''
'''def add(a,b,c):
    return (a+b+c)
a=10
b=20
print(add(a,b,c=5))#c is default parameter'''
'''def add(*b):
    return (b)
a=10
b=20
c=30
print(add(a,b,c,28,90))'''
'''def add():
    a=11#local variable
    print("inside",a)
a=10#it is different from function def a
print('before ',a)
add()
print('after',a)'''
'''def add():
    global b
    b=88
    print('inside',b)
a=10
print('before',a)
add()
print('after',b)'''
'''import math
a=4
b=6
k=math.gcd(a,b)
lcm=a*b//k
print(lcm)'''
'''def lcm(a,b):
     c=b
     while True:
         if c%a==0 and c%b==0:
             return c
         c+=1
a,b=map(int,input().split())
print(lcm(a,b))'''
a,b=map(int,input().split())
lcm=0
gcd=0
for i in range(2,b+1):
    if a%i==0 and b%i==0:
        gcd=i
lcm=a*b//gcd
print(lcm)





