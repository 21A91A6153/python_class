''''
case1:input all small ww:ii:pp:rr:oo
output:capitals lo
case:2 zx:za:ee
26-24=2 return b
'''
a=input()
s=''
for i in range(0,len(a),3):
    if a[i]==a[i+1]:
        s+=chr(ord(a[i])-32)
    else:
        b=ord(max(a[i:i+2]))-ord(min(a[i:i+2]))
        s+=chr(64+b)
print(s)
