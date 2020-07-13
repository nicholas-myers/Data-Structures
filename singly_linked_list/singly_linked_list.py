class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
    
# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            
    def contains(self, value):
        
        current = self.head
        while current is not value:
            current = current.get_next()
            if current.get_value() == value:
                return True
            
            
            
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        val = self.tail.get_value()
        self.tail = current
        return val