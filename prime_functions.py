def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if prime(n):
    a=n
    d=0
    pd=0
    while n:
        r=n%10
        n//=10
        d+=1
        if prime(r):
            pd+=1
    if d==pd:
        print(a,'mega Prime')
    else:
        print(a,'not mega prime')
        
