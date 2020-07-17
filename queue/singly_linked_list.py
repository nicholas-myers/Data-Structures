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
    
    def __str__(self):
        return f"{self.value}, {self.next}"
    
# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))

# print(type(ll))
        
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
        # check if list is empty
        if not self.head:
            return False
        current = self.head
        # current exists and is truthy so it will loop through the whole list
        while current:
            # if the value becomes current then return true
            if current.get_value() is value:
                return True
            current = current.get_next()
        # if we get to the end and did not find value return false
        return False
        
    def remove_head(self):
        # if there is no list stop the function
        if self.head is None and self.tail is None:
                return
        if not self.head.get_next():
            head = self.head 
            # delete the linked list's head reference 
            self.head = None
            # also delete the linked list's tail reference 
            self.tail = None 
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head 
        self.head = self.head.get_next()
        return val
        
    def get_max(self):
        # if there is no list stop the function
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

