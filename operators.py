Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hi","pravallika",end="\n")
hi pravallika
print('hi','hello',sep='-')
hi-hello
a=10
b=20.5
print("%d",a,"%f",b)
%d 10 %f 20.5
print("%d"%a,"%f"%b)
10 20.500000
print("%d"%a,".%2f"%b)
10 .20.500000
print("%.2f"%b)
20.50
print("%d"%a,"%.2f"%b)
10 20.50
5||2
SyntaxError: invalid syntax

a=5
b=6
~a
-6
~b
-7
a&&b
SyntaxError: invalid syntax
a&b
4
a<<2
20
a>>2
1
a and b
6
6a={20,30,40]
SyntaxError: invalid decimal literal
a=[20,40,50]
20 in a
True
10 in a
False
10 not in a
True
a=6
b=6
a is b
True
b is a
True
a is not b
False
id9a0
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    id9a0
NameError: name 'id9a0' is not defined
id(a)
3033009291664
id(b)
3033009291664
3033009291664a=10
SyntaxError: invalid decimal literal
a=10
b=20
a||b
SyntaxError: invalid syntax
a//b
0
a**b
100000000000000000000
b**a
10240000000000
