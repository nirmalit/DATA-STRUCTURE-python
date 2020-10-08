class Tree:
    def __init__(self,val):
        self.data=val
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        self.level=0
        parent=self.parent
        while parent!=None:
            self.level+=1
            parent=parent.parent
        return self.level

    def printTree(self):
        print(" "*self.get_level(),end="")
        if self.get_level()==0:
            print(self.data)
        else:
            print("|__",self.data)
        if len(self.children)>0:
            for x in self.children:
                x.printTree()


root=Tree("electronic")
m_root=Tree("laptop")
lg=Tree("LG")
smg=Tree("Samsung")
m_root.add_child(lg)
m_root.add_child(smg)
root.add_child(m_root)
m1_root=Tree("fridge")
root.add_child(m1_root)
root.printTree()




