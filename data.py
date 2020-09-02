class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
class Single:
    def __init__(self,val):
        self.head = val

    def printlist(self):
        self.l = self.head
        while self.l is not None:
            print(self.l.value)
            self.l=self.l.next

    def insert_at_begin(self,val):
        e=Node(val)
        e.next=self.head
        self.head=e

    def insert_at_end(self,val):
        e=Node(val)
        self.last=self.head
        while self.last.next is not None:
            self.last=self.last.next
        self.last.next=e

    def insert_at_index(self,val,index):
        e=Node(val)
        self.i=0
        self.previous_node=self.head
        while(self.i<index):
            self.previous_node=self.previous_node.next
            self.i+=1
        e.next=self.previous_node.next
        self.previous_node.next=e

    def remove_element(self,val):
        self.previous_node=self.head
        if self.previous_node.value==val:
            self.head=self.previous_node.next
            return
        while self.previous_node.next.value != val:
            self.previous_node=self.previous_node.next
        self.current=self.previous_node.next
        self.previous_node.next=self.current.next

#creating node e1,e2,e3,e4
e1=Node("1")
e2=Node("2")
e3=Node("3")
e4=Node("4")

#linking nodes e1 -> e2 -> e3 -> e4
e1.next= e2
e2.next= e3
e3.next=e4
list1=Single(e1)

print("Before Insertion")
list1.printlist()
list1.remove_element("4")

print("After removing")
list1.printlist()
