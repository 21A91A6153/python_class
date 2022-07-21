#tkinter used to develop apps
'''import tkinter as tk #as-alias in function
a=tk.Tk()#create interface
a.mainloop()#how much time must be active;while loop condition'''


#import tkinter as tk
#a=tk.Tk()
#a.title('BTS')
#t=tk.Toplevel()
#t.title('submit')
#a.mainloop()

#b=tk.Button(a,text='submit1',fg='red')
#b.pack(side='left')
#c=tk.Button(a,text='submit2',fg='blue')#forground:fg
#c.pack(side='left')#rendu same side estey side by side vastadi
#a.mainloop()

'''b=tk.Button(a,text='Submit1',fg='red')
#b.grid(row=0,column=0)
b.place(x=10,y=10)
c=tk.Button(a,text='Submit2',fg='green')
#c.grid(row=1,column=1)
c.place(x=10,y=10)
a.mainloop()'''
'''
l=tk.Label(a,text='first name',fg='white',bg='black')
l.grid(row=0,column=0)
e=tk.Entry(a)
e.grid(row=0,column=1)
l1=tk.Label(a,text='last name',fg='white',bg='purple')
l1.grid(row=1,column=0)
e1=tk.Entry(a)
e1.grid(row=1,column=1)
a.mainloop()'''


##c=tk.Checkbutton(a,text='c')
##c.grid(row=0,column=0)
##c1=tk.Checkbutton(a,text='python')
##c1.grid(row=1,column=1)
##a.mainloop()

##l=tk.Listbox(a)
##l.insert(1,'c')
##l.insert(2,'cpp')
##l.insert(3,'java')
##l.insert(4,'python')
##l.pack()
##a.mainloop()

##a.geometry('200x150')#size change
##s=tk.Spinbox(a,from_=10,to=20)
##s.pack()
##a.mainloop()

##a.geometry('200x150')
##f=tk.LabelFrame(a,text='this is frame')
##f.pack(fill='both',expand='yes')
##l=tk.Label(f,text='Tkinter example')
##l.pack()
##a.mainloop()

##import tkinter as tk
##from tkinter import messagebox
##a=tk.Tk()
##a.title('BTS')
##a.geometry('300x200')
##def example():
##      #messagebox.showinfo('hi','login Successful')
##      #messagebox.showerror('invalid')
##      #messagebox.showwarning('warning')
##      #messagebox.askyesno('hi')
##       messagebox.askquestion('what')   
##p=tk.Button(a,text="submit",command=example)#command=a.destroy)
##p.pack()
##a.mainloop()

#----------------Build a calender-----------------

'''from tkinter import *
import tkinter as tk
import calendar
r = tk.Tk()
r.geometry('400x300')
r.title('calender')

def show():
    m=int(month.get())
    y=int(year.get())
    output = calendar.month(y,m)
    cal.insert('end',output)
def clear():
    cal.delete(1.0,'end')
def exit():
    r.destroy()

m_label = Label(r,text="month",font=('verdana','10','bold'))
m_label.place(x=70,y=80)

month = Spinbox(r, from_=1, to = 12,width='5')
month.place(x=140,y=80)

y_label = Label(r,text='year')
y_label.place(x=210,y=80)

year = Spinbox(r, from_=2020, to = 3000,width='8')
year.place(x=260,y=80)

cal = Text(r,width=33,height=8,relief=RIDGE,borderwidth=2)
cal.place(x=70,y=110)

show = Button(r,text='Show',command=show)
show.place(x=140,y=250)

clear = Button(r,text="clear",command=clear)
clear.place(x=200,y=250)

exit = Button(r,text='Exit',command=exit)
exit.place(x=260,y=250)
r.mainloop()'''


         

    











