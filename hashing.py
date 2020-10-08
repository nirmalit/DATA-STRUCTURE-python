class hash:
    def __init__(self):
        self.size=10
        self.arr=[[] for x in range(self.size)]

    def getindex(self,key):
        self.h=0
        for x in key:
            self.h+=ord(x)
        return self.h%10

    def __setitem__(self, key, value):
        self.idx=self.getindex(key)
        self.arr[self.idx].append([key,value])
        return
    def deleteitem(self, key):
        self.idx=self.getindex(key)
        for x in self.arr[self.idx]:
            if x[0]==key:
                self.arr[self.idx].remove(x)
                return
        print("Element is not in the hash table")

    def get_value(self,key):
        self.idx = self.getindex(key)
        val=self.arr[self.idx]
        return val
    def print_value(self):
        print(self.arr)

temp=hash()
temp["mar 23"]=10 #equal to temp.setitem("mar 23",10)
print(temp.getindex("mar 23"))
temp["march 6"]=12
temp["march 17"]=13
temp.print_value()
temp.deleteitem("march 6")
temp.print_value()
