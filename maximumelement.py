'''a=list(map(int,input().split()))
maxs=0
for i in a:
    if maxs<i:
        maxs=i
print(maxs)
m=a[0]
for i in range(len(a)):
    if m>a[i]:
        m=a[i]
print(m)'''
#duplicates
#a=list(map(int,input().split()))
'''c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[i])'''

b=[]
a=list(map(int,input().split()))
for i in a:
    if i not in b and a.count(i)>1:
        b.append(i)
if b==[]:
    print(-1)
else:
    for i in b:#*b
        print(i)
