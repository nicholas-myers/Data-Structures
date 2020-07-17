from singly_linked_list import LinkedList

n = 10000

l = [i for in range(n)]
ll = LinkedList()

for i in range(n):
    ll.add_to_tail(i)
    
start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked List took {end_time - start_time} seconds")
start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked List took {end_time - start_time} seconds")