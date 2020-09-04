class Stack:
    def __init__(self):
        self.stack=[]

    def add(self,val):
        self.stack.append(val)

    def print_stack(self):
        for x in self.stack:
            print(x,end=" ")
        print("")
    def remove(self):
        if len(self.stack)<=0:
            print("There is no element in stack")
        else:
            self.stack.pop()
s1=Stack()
s1.add(1)
s1.add(2)
s1.add(3)
print("before pop")
s1.print_stack()
print("After pop")
s1.remove()
s1.print_stack()
