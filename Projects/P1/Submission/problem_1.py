class Node:
    def __init__ (self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def prepend (self, val):
        node = self.head
        
        if node is None:
            self.head = Node(val)
            self.tail = self.head
            self.tail.prev = self.head
            return
        
        self.head = Node(val)
        self.head.next = node
        node.prev = self.head

    def remove (self, val):
        node = self.head
        
        if node is None: return
        
        if node.data == val:
            self.head = self.head.next
            return
        
        while (node.next):
            if node.next.data == val:
                node.next = node.next.next
                return
            
            node = node.next
        
    def pop (self):
        node = self.tail
        self.tail = node.prev
        self.tail.next = None
        
        return node.data
    
    def size (self):
        node = self.head
        answer = 0
        
        while node:
            answer += 1
            node = node.next
            
        return answer
        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.list = LinkedList()
        self.dict = dict()
        self.cap = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        answer = self.dict.get(key)
        
        if answer:
            return answer
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        
        if self.dict.get(key): return
        
        if self.cap == self.list.size():
            old = self.list.pop()
            del self.dict[old]
            
        self.list.remove(key)
        self.list.prepend(key)
        self.dict[key] = value

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1