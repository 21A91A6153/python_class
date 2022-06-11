'''d={}
for i in range(1,6):
    d[i]=i*i
print(d)'''
'''b=[3 for i in range(1,6)]
print(b)#element 3 repeated 5 times'''
#b=[i*i for i in range(1,6)]
#print(b)
#b=[ i for i in range(1,11) if i%2==0]
#print(b)
'''b=[i for i in range(1,11)]
d={i:i*i for i in range(1,6)}
print(d)'''
''''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in a:#common elements
    for j in b:
        if i==j:
            print(i,end=" ")'''
#common elements
'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    for i in b:
        c.append(i)
print(*c)'''
#unique elements
'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c=set(c)
for i in c:
    if i in a and i in b:
        continue
    else:
        print(i,end=" ")'''
#union #intersection #difference
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=set(a)
b=set(b)
#a=a.union(b)
#a=a.intersection(b)
a=a.difference(b)
print(a)




        
            

