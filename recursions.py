n=int(input())#decimal to binary
def dec(n):
    s=' '
    while n>1:#
         d=n%2#9-1
         n=n//2#4-0#
         s+=str(d)
    s+=str(n)
    return s[ : :-1]
print(dec(n))
''''def binary(n):#binary to decimal
    sums=0
    i=0
    while(n):
        d=n%10
        n=n//10
        sums=sums+((2**d)*i)
        i+=1
    return sums
n=int(input())
print(binary(n))'''
