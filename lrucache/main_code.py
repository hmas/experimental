# LRU Cache Implementation in Python

from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the cache with a fixed capacity
        self.capacity = capacity
        self.cache = OrderedDict()  # This will store the keys and values in order of usage

    def get(self, key: int) -> Optional[int]:
        # Returns the value for the key if it exists in cache, otherwise -1.
        if key not in self.cache:
            return -1  # Key not found
        else:
            # Move the accessed item to the end of the OrderedDict to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value associated with the key

    def put(self, key: int, value: str):
        # Update or add the value for the key.
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the existing key to the end
        self.cache[key] = value  # Insert/Update the key-value pair
        if len(self.cache) > self.capacity:
            # Remove the first item (least recently used)
            self.cache.popitem(last=False)  # Remove the first item from the OrderedDict

# Unit Tests
import unittest

class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        # Create an LRU Cache with capacity 2
        lru_cache = LRUCache(2)
        lru_cache.put(1, 'A')  # Cache is {1: 'A'}
        lru_cache.put(2, 'B')  # Cache is {1: 'A', 2: 'B'}
        self.assertEqual(lru_cache.get(1), 'A')  # Returns 'A'
        lru_cache.put(3, 'C')  # Evicts key 2, Cache is {1: 'A', 3: 'C'}
        self.assertEqual(lru_cache.get(2), -1)  # Returns -1 (not found)
        lru_cache.put(4, 'D')  # Evicts key 1, Cache is {3: 'C', 4: 'D'}
        self.assertEqual(lru_cache.get(1), -1)  # Returns -1 (not found)
        self.assertEqual(lru_cache.get(3), 'C')  # Returns 'C'
        self.assertEqual(lru_cache.get(4), 'D')  # Returns 'D'

# Stress Test
if __name__ == '__main__':
    import time
    start_time = time.time()
    lru_cache = LRUCache(1000)  # Create a large cache
    for i in range(2000):  # Insert more items than capacity
        lru_cache.put(i, str(i))
    print("Stress test completed in: ", time.time() - start_time)

    # Run unit tests
    unittest.main(argv=[''], exit=False)  # Run the tests without exiting the interpreter