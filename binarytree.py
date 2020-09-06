class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

    def insert(self,val):
        if self.data:
            if self.data>val:
                if self.left is None:
                    self.left=Node(val)
                else:
                    self.left.insert(val)
            elif self.data<val:
                if self.right is None:
                    self.right=Node(val)
                else:
                    self.right.insert(val)
            else:
                print("The value is already in the list")
        else:
            self.data=val
    def search(self,val):
        if self.data==val:
            return "{} is found ".format(val)
        elif self.data>val:
            if self.left is None:
                return "{} is not found ".format(val)
            return self.left.search(val)
        elif self.data<val:
            if self.right is None:
                return "{} is not found ".format(val)
            return self.right.search(val)


    def print_list(self):
        if self.data:
            if self.left is not None:
                self.left.print_list()
            print(self.data)
            if self.right is not None:
                self.right.print_list()


t=Node(2)
t.insert(1)
t.insert(3)
t.print_list()
print(t.search(0))
