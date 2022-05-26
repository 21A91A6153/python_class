n=int(input())
c=0
k=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    while(n):
        d=n%10
        for j in range(1,n+1):
            if d%j==0:
                k=k+1
        n=n//10
if c==2 and k==4:
    print("Mega")
else:
    print("Not")
                    
                
