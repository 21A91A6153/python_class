a=int(input())
b=int(input())
for i in range(a,b+1):
    if i%2==1:
        continue
    print(i,end=' ')