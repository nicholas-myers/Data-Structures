"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) < 1:
#             return None
#         return self.storage.pop()
    
#     def __str__(self):
#         return f"{self.storage}"
    
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_tail()
        return None
    
    def __str__(self):
        return f"{self.storage}"
    
    
# new_stack = Stack()

# print(new_stack)
# new_stack.push(100)
# new_stack.push(101)
# new_stack.push(102)
# new_stack.push(103)
# new_stack.push(104)
# new_stack.push(105)
# print(new_stack.pop())