# Cyclic Doubly Linked List

class Node:
    def __init__(self, pred=None, succ=None, data=None):
        self.pred = pred
        self.succ = succ
        self.data = data

class CyclicDoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.length = 0

    # string representation
    def __str__(self):
        str = "<"
        nd = self.start_node
        for i in range(self.length):
            str += repr(nd.data)
            if i < self.length-1: str += ", "
            nd = nd.succ
        str += ">"
        return str

    def iterate(self, times=None):
        nd = self.start_node
        yield nd.data
        ct = 1
        while nd.succ and (ct < times or not times):
            nd = nd.succ
            ct += 1
            yield nd.data
        return

    # inserts a node before the start node
    # if list is empty, a self-referencing node is added
    def append(self, data):
        newNode = Node(None,None,data)
        if not self.start_node: # empty list
            newNode.pred = newNode
            newNode.succ = newNode
            self.start_node = newNode
        else:
            newNode.succ = self.start_node
            newNode.pred = self.start_node.pred
            self.start_node.pred.succ = newNode
            self.start_node.pred = newNode
        self.length += 1
        return newNode

    def insert_after(self, ref, data):
        nd = self.start_node
        ct = 0
        nd = ref
#        while nd is not ref:
#            nd = nd.succ
#            ct += 1
#            if ct > self.length:
#                print("Error: Tried to insert element after non-existing element.")
#                return None
        newNode = Node(pred=nd, succ=nd.succ, data=data)
        nd.succ.pred = newNode
        nd.succ = newNode
        self.length += 1
        return newNode

    def remove(self, node):
        if node == None:
            print("Error: Node is None, bro")
            return
        if not self.start_node:
            print("Error: Tried to remove element from empty list.")
            return
#        ct = 0
#        nd = node
#        while nd is not node:
#            nd = nd.succ
#            ct += 1
#            if ct > self.length:
#                print("Error: Tried to remove non-existing element.")
#                return
        node.succ.pred = node.pred
        node.pred.succ = node.succ
        if node == self.start_node:
            if self.length > 1:
                self.start_node = node.succ
            else:
                self.start_node = None
        # set node's succ and pred to None to avoid problems
        node.pred = node.succ = None
        self.length -= 1
