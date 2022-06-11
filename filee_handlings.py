#a=open(r'C:\Users\lenovo\Desktop\example.txt','a')#x-create file
#a.write('but online clsses')
#a.close()'''
#w-write,create  ,a-create,write,r=read,r+-readwrite,w+-write,read
#a+-write,read

#       new line
#a=open(r'C:\Users\lenovo\Desktop\example.txt','w')#x-create file
#a.write('but online clsses\n')
#a.write('heat')
#a.close()
#          list

#l=['hi\n','this\n','is\n','bts']
#a=open(r'C:\Users\lenovo\Desktop\example.txt','w')
#for i in l:
#a.writelines(l)
#a.close()

#with open(r'C:\Users\lenovo\Desktop\example.txt','w') as f:
#   f.writelines(l)
#    f.close()

#a=open(r'C:\Users\lenovo\Desktop\example.txt','r')
#b=a.read()#to read the content,though we have multiple line,it reads in singlel
#print(b)
#b=a.readlines()#read data in multiple lines,individual lines
#for i in b:
 #   print(i)
#a.close()
 
#a=open(r'C:\Users\lenovo\Desktop\example.csv','w')
#a.write('heat')
#a.write('but')
#a.close()

#a=open(r'C:\Users\lenovo\Desktop\cars.csv','r')
#b=a.readlines()
#c=[]
#for i in b:
 #   i=i.split(',')
  #  c.append(i)
#s=set()
#for i in c[1:]:
 #   s.add(i[-1])
#d=0
#for i in c[1:]:
 #   if i[2]=='8':
  #      d+=1
#print(d)
#for i in c[1:]:
 #   if i[2]=='8' and i[-2]=='70':
  #      d=d+1
   #     print(i[0])
#print(d)
   
#            exemption handling:
# error : it stops the file to execute;3 types error
#syntax error:rules and regulations properly
#logical error:no syntax error,but no proper output->a=10 print(a+b)
#run time error:file not found
#try:we will put a block of code

#try:
 #   a=10
  #  print(a+b)#if no error:try executed,otherwise except execute
#except:
 #   print('hi')

'''try:
    a=10
    print(a)
    #print(a+b)
    #print(a/0)
    #print(a)
except NameError:
    print('give proper name')
except ZeroDivisionError:
    print("can't divide")
else:
    print("hi")
finally:
    print('done')'''

'''a=float(input())
if(a>=0 and a<=10):
    print("my gpa:",a)
else:
    raise Exception('entervalid')'''
     





   
        
   
