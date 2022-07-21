'''def rever(a):
    str1=""
    for i in range(len(a)-1,-1,-1):
        str1=str1+a[i]
    return str1
a='python'
print(rever(a))'''

'''a='python'
a=a[::-1]
print(a)'''

'''a='python'
a=reversed(a)
a=''.join(a)
print(a)'''

def rever(a):
    if len(a)==0:
        return a
    else:
        return rever(a[1:])+a[0]
    
a='python'
print(rever(a))

'''a='python'
k=len(a)
s=''
while k>0:
    s=s+str(a[k-1])
    k-=1
print(s)'''


