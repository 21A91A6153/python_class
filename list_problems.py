a=list(map(int,input().split()))#length =odd

if len(a)%2==1:
    m=(len(a)//2)+1
else:
    m=len(a)//2
'''
s=True
for i in range(m-1):
    if a[i]<a[i+1]:
        s=True
    else:
        s=False
        break
if s:
    for i in range(m+1,len(a)-1):
        if a[i]>a[i+1]:
            s=True
        else:
           s=False
           break
    print(s)
else:
   print(s)'''
if a[:m+1]==sorted(a[:m+1]) and a[m+1:]==sorted(a[m+1:],reverse=True):
    if a[m]<a[m+1]:
        print(True)
    else:
        print(False)
else:
    print(False)
    
