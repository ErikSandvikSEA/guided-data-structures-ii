class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_value(self):
        # returns the node's data
        return self.data

    def get_next(self):
        # returns the thing pointed at by the node's `next` reference
        return self.next

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next = new_next


class LinkedList:
    def __init__(self)
    # the first Node in the LinkedList 
    self.head = None
    # the last Node in the LinkedList 
    self.tail = None 

    def add_to_tail(self, data):
        # addss `data` to the end of the LinkedList 
        # wrap the `data` in a Node instance 
        new_node = Node(data)


        # call set_next with the new_node on the current tail node 
        self.tail.set_next(new_node)
        # update self.tail to point to the new last Node in the LinkedList 
        self.tail = new_node 




node = Node(1)
node.set_next(Node(2))
node.get_next().set_next(Node(3))
node.get_next().get_next().set_next(Node(4))
# YUCK

