class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        if len(self.items)!=0:
            return self.items[-1]
    def display(self):
        print(self.items)
a='python'
b=' '
st=Stack()
for i in range(len(a)):
    st.push(a[i])
for i in range(len(a)):
    b+=st.pop()
    print(b)


