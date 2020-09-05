class Node:
    def __init__(self,val):
        self.data=val
        self.prev_node=None
        self.next_node=None

class doubleLL:
    def __init__(self):
        self.head=None

    def add(self,val):
        new_node=Node(val)
        if self.head is not None:
            new_node.next_node=self.head
            self.head.prev_node=new_node
        self.head=new_node

    def remove(self,val):
        temp=self.head
        #if the val at begining
        if temp.data==val:
            self.head=temp.next_node
            return
        while temp.data != val:
            temp=temp.next_node
        prev = temp.prev_node
        after = temp.next_node
        #if val at end
        if after is None:
            prev.next_node=None
            return
        #if val at middle
        prev.next_node=after
        after.prev_node= prev

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next_node
        print("")

dll=doubleLL()
n=Node(1)
dll.head=n
dll.add(2)
dll.add(3)
print("element in the list")
dll.print_list()
dll.remove(3)
print("element in the list after deleting")
dll.print_list()