'''n=int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end=" ")
    print()'''
'''n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("@",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()'''
'''umid=input()
upw=int(input())
dmid='thub@123.com'
dpw=1234
if dmid==umid and dpw==upw:
        print('login succesful')
else:
        print("wrong ")'''
'''
dmid='thub@123.com'
dpw=1234
for i in range(5):
      umid=input()
      upw=int(input())
      if dmid==umid and dpw==upw:
        print('login succesful')
        break
      else:
        print("wrong ")
else:
    print("temporarly Blocked")'''
'''n=int(input())
c=0
i=1
k=n*n
while(i<=pow(k,0.5)):
    if n%i==0:
        c=c+1
    i=i+1
if(c==2):
   print('prime')
else:
    print('not')'''
'''n=int(input())
for i in range(2,n):#(2,n//2+1),(2,sqrt(n)+1)
    if n%i==0:
        print('not')
        break
else:
    print("prime")'''
'''n,r=map(int,input().split())
s=1
c=0
if n>r:
    s=-1
for i in range(n,r+s,s):
    for j in range(1,int(pow(i*i,0.5)+1)):
        if i%j==0:
            c=c+1
    if c==2:
        print(i,end=" ")
    c=0'''
n=int(input())
for i in range(n,1,-1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
           break
    else:
        print(i,end=' ')
        break
'''n=int(input())
k=-1
while(n>1):
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            break
    else:
        print(n,end=' ')
        break
    n=n+k'''
'''n=int(input())
k=1
while(n>1):
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            break
    else:
        print(n,end=' ')
        break
    n=n+k'''
'''n=int(input())
for i in range(n,n*n):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
           break
    else:
        print(i,end=' ')
        break'''


            
            
            
            






