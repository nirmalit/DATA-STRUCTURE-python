class Queue:
    def __init__(self):
        self.queue=[]

    def add_to_queue(self,val):
        self.queue.append(val)

    def remove_from_queue(self):
        if len(self.queue):
            self.queue.pop(0)
            return
        print("Queue is empty")

    def print_queue(self):
        if len(self.queue):
            for x in self.queue:
                print(x,end=" ")
            print("")
            return
        print("Queue has no element")
q1=Queue()
q1.add_to_queue(1)
q1.add_to_queue(2)
q1.add_to_queue(3)
print("element is queue ")
q1.print_queue()
q1.remove_from_queue()
print("element in queue after dequeue ")
q1.print_queue()

