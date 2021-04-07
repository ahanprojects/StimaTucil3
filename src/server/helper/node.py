class Node:

    # constructor
    def __init__(self, name, position, parent):
        self.name = name
        self.position = position    # tuple (x,y)
        self.parent = parent        # node sebelumnya
        self.connected = []         # array of tuple,format (nama,bobot)
        self.g = 0                  # jarak ke node awal melalui node-node sebelumnya
        self.h = 0                  # jarak heuristik ke node tujuan
        self.f = 0                  # f(n)
    
    # setter
    def appendToconnected(self,tuple):
        self.connected.append(tuple)

    def setg(self,g):
        self.g = g
    
    def seth(self,h):
        self.h = h
    
    def setf(self,f):
        self.f = f
    
    def setParent(self,parent_node):
        self.parent = parent_node

    # getter
    def getName(self):
        return self.name

    def getg(self):
        return self.g
    
    def geth(self):
        return self.h
    
    def getf(self):
        return self.f
    
    def getParent(self):
        return self.parent

    def getConnected(self):
        return self.connected

    def getCoord(self):
        return self.position

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
         
    # Print node
    def __repr__(self):
        a = "Node : "+self.name+" "+str(self.position)+"\n"
        pr = self.parent.getName() if not self.parent is None else "None"
        b = "Parent : "+pr+'\n'
        c = "Connected to :"+str(self.connected)
        return a + b + c