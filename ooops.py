#ooops:it is a object oriented
#it contains class
#class:blue print of objects and methods we access through objects,n no of func
#object:particular instance of clss
#default in class:constructor that will be executed even if we don't call
#basic structure of class
'''class car():
    def _init_(self):#constructor
         print('hi')
    def display(self):#instances
        print('hello')
a=car()#object
a.display()
b=car()'''


#self:particular object
'''class car():
    def _init_(self,name,model):#(a,kia,123)
        self.name=name#instance variables or local variables
        self.model=model
    def display(self):
        print(self.name,self.model)
a=car('kia',123)
a.display()
a.name:particular ga kavali antey ela call cheyali'''
'''class Student():
    college='Aditya'#static /class:it is fixed
    def __init__(self,name,roll,s1,s2):
        self.name=name
        self.roll=roll
        self.s1=s1
        self.s2=s2
        #self.college=college
    def display(self):
        print(self.name,self.roll,(self.s1+self.s2)//2,self.college)
        
a=Student('sachin',53,35,45)
a.display()
print((a.s1+a.s2)//2)
print(a.college)'''
#@classmethod:def classm(cls)cls:particular indicaion:highest priority to cls variable
#it is strict and doesn't go to instance variable
'''class Student():
    college='Aditya'#static /class:it is fixed
    def __init__(self,name,roll,s1,s2,college):
        self.name=name
        self.roll=roll
        self.s1=s1
        self.s2=s2
        self.college=college
    def display(self):
        print(self.name,self.roll,(self.s1+self.s2)//2,self.college)
    @classmethod
    def classm(cls):
        cls.college='ACET'
        #print(cls.college)
    @staticmethod
    def staticm():
        print('done')

#a.display()
#a.classm()#call reference name tho call cheyachu we can modify cls variable
#Student.classm()#call
#a.staticm()#
#Student.staticm()#object lekapoyina cheyachu
a=Student('sachin',53,45,67,'AEC')
a.display()
#a.classm()'''
'''class Student():
    def __init__(self,name,aadhar,roll):
        self.name=name
        self.aadhar=aadhar
        self.roll=roll
    def display(self):
        print(self.name,self.aadhar,self.roll)
a=Student('sachin',113456789,65)
a.display()'''
'''class Person():
    college='AEC'
    def __init__(self,name,aadhar):
        self.name=name
        self.aadhar=aadhar
        #self.college=college
    def display(self):
        print(self.name,self.aadhar)

class Student(Person):
    #college='AEC'
    def __init__(self,name,roll,aadhar,college):
        self.roll=roll
        #self.college=college
        super().__init__(name,aadhar)
    def display(self):
        print(self.name,self.aadhar,self.roll,self.college)
a=Student('sachin',113456789,65,'aec')
a.display()'''

#inheritance:by default we can get properties from another
'''class person():
    #college='AEC'
    def __init__(self,name,aadhar):
        self.name=name
        self.aadhar=aadhar
        #self.college=college
    def display(self):
        print(self.name,self.aadhar)
class Student(person):
    def __init__(self,name,aadhar,roll,avg):
        self.roll=roll
        self.avg=avg
        super().__init__(name,aadhar)
    def display(self):
        print(self.roll,self.avg,self.name,self.roll)
a=Student('qwerty',1234,789,89.08)
a.display()'''
#preference :child instance,parent instance,child cls,parent cls

'''class person():
    #college='AEC'
    def __init__(self,name,aadhar,college):
        self.name=name
        self.aadhar=aadhar
        self.college=college
    def display(self):
        print(self.name,self.aadhar)
class Student(person):
    college='AEC'
    def __init__(self,name,aadhar,roll,avg,college):
        self.roll=roll
        self.avg=avg
        #self.college=college
        super().__init__(name,aadhar,college)
    def display(self):
        print(self.roll,self.avg,self.name,self.aadhar,self.college)
a=Student('xyz',1234,789,78.09,'aditya')
a.display()'''
#polymorphism:- many forms
class coding:
    def info(self):
        print('c,cpp,java,python')
    def syntax(self):
        print('programming languages have different syntaxes')
class pythonn(coding):
    def syntax(self):
        print('python has indentation')
class javaa(coding):
    def syntax(self):
        print('java has brackets in syntax')
a=coding()#object for parent
a.info()
a.syntax()

b=pythonn()
b.info()
b.syntax()

c=javaa()
c.info()
c.syntax()




        



    
