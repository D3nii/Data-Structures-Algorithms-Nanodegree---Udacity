from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.data = OrderedDict()
        self.cap = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            val = self.data.pop(key)
            self.data[key] = val
            return val
        
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        
        if self.capacity == 0: return

        if key in self.data:
            val = self.data.pop(key)
            self.data[key] = val
        else:
            if len(self.data) < self.capacity:
                self.data[key] = val
            else:
                self.data.popitem(last = False)
                self.data[key] = val

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1)) # returns 1
print(our_cache.get(2)) # returns 2
print(our_cache.get(9)) # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.get(4) # Expected Value = 4
our_cache.get(1) # Expected Value = -1
our_cache.set(2,4)
print(our_cache.get(2)) # Expected Value = 4 Your Output = 2

# Edge Cases:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1)) # should return 10
print(our_cache.get(2)) # should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1) # should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1)) # should return -1