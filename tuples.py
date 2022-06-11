#for list we have sort
#
#tuple--->cant be change(it is fixed one)(immutable)
#declaration of tuple:-->()paranthesis
#by using index positions we can access tuple
#a.append(),del a,remove(),extend
"""
"""
a=(1,2,3,4,5)
ex: a[0:2]-->1,2
a[0: ]-->1,2,3,4,5
"""
#reverse in tuple:-->a[::-1]
#len(a),max(A),min(a),a.count(2),a.index(6),sorted(a)-->only for seeing it dont modify original elemts
#a.sort()-->uses for sorted a list
#entire deletion is possible in tuples-->but not single elements
#advantage of tuples:-->immutable
"""
modify of tuple:we cant modify in tuple
"""
#how to run a loop on tuple:
#use in privacy and security
#only tuple uses acces of elements
"""
a=tuple(map(int,input().split()))---->()
print(len(a),max(a))
for i in a:
    print(i,end=" ")
print()
for i in range(len(a)):
    print(i,a[i],end=' ')
    print()
"""
#set-->sets are unordered list without duplicate values---{}
#declaration os set-->{}-->a={1,2,3,4,5,1,0}
#no index order in set-->bcz of unorderd 
#repetations not allow in set
#ex:a.count(any element)-->always one
#u cant add existing element-->a.add()
#a.remove(element)-->it allows in set,,entire del set--->del a
#....................................................................................
"""
a=list(map(int,input().split()))#1 2 3 4 
b=list(map(int,input().split()))# 4 5
for i in b:
    if i not in a:
        a.append(i)#5
print(a)#1 2 3 4 5
"""
#remove duplicates using set
"""
a=list(map(int,input().split()))#1 2 3 4 
b=list(map(int,input().split()))
print(*set(a+b))
"""
#chararecter base strings we cant convert into int
#we can typecast core data types also
#type casting:
"""
a=[1,2,3,4,5]
b=set(a)
c=tuple(a)
"""
#Dictionary
"""
key must be an integer or string or float
key is something like an index place
val is anything-->string,int,float,boolean,list,set,tuple,dictionary
d={key:value}--->dictionary element---->{}
    0     1    2----->index
d={0:11,1:22,2:33}-->key and value pair
len(d)--->3
binding of key and value together both we can call it as a element
by using key we can access value in dictionaries
access:-->a[key]-->we can access multiple values at a time
modify--->yes
##examples:
  d={'s1':[11,22,33],'s2':[44,55]}
  d[1.2]
  [11, 22, 33]
   d[1.2]={11,22}
   d[1.2]
   {11, 22}
a['s1'].append(22)
a['s1'][0]=8
a['s1']=88
loop reading for dictionary->a.keys()-->keys
a.values()--->values
a.items()--->both keys and values
modify:a[key]=new valuse,a.add([key:value])
"""
#example:
"""
a={'s1':[33,43],'s2':[55,66]}
a['s3']:[77,11]
a
output:-->a={'s1':[33,43],'s2':[55,66],'s3':[77,11]}
"""
#if we add more than one elemnts in dictionary there we use:
"""
a={'s1':[33,43],'s2':[55,66]}
b={'s3':77,'s5':66}
a.update(b)
"""
#delete any particular element in dic us del
"""
del a['s1']---->del a[key]
"""
#how to take a customise dic:
"""
no customize dic we can give 
"""
#how to run a loop on dictionary
#we have three methods

"""
x=set()
x
"""
#display how many times
"""
a=[2,2,3,3,3,4,5,1]
b=[]
c=0
for i in a:
    c=0
    if i in b:
        continue
    for j in a:
        if i==j:
            c+=1
            b=[i]
    print(i,':',c)
"""
#display how many times
"""
a=[2,2,3,3,3,4,5,1]
b=set(a)
for i in b:
    print(i,a.count(i))
"""
#diplay how many times element is repeated in dictionary
"""
a=[2,2,3,3,3,4,5,1]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
