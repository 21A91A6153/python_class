n=int(input())
#temp=n
#rev=0
def prime(n):
     for i in range(2,int(n**0.5)+1):
          if n%i==0:
             return False
          else:
             return True
'''while(n!=0):
    d=n%10
    n=n//10
    rev=rev*10+d
print(prime(temp))
print(prime(rev))
if prime(temp) and prime(rev):
    print("Twisted")
else:
    print("Not")'''
if prime(n):
    r=0
    while n:
        rem=n%10
        n=n//10
        r=r*10+rem
    if prime(r):
        print("twisted")
    else:
        print("Not ")
else:
    print("Not")
    
    
        
    
