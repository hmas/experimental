# LRU Cache Implementation in Python

from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        """Initialize the LRUCache with a given capacity."""
        self.capacity = capacity  # Maximum capacity of the cache
        self.cache = OrderedDict()  # Dictionary to store key-value pairs in order of usage

    def get(self, key: int) -> Optional[int]:
        """Returns the value for the key if it exists in cache, otherwise -1."""
        if key not in self.cache:
            return -1  # Key not found
        else:
            self.cache.move_to_end(key)  # Move the accessed item to the end (most recently used)
            return self.cache[key]  # Return the value associated with the key

    def put(self, key: int, value: str):
        """Update or add the value for the key."""
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the accessed item to the end
        self.cache[key] = value  # Update or add the key-value pair
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first item (least recently used)

# Unit tests for LRUCache
import unittest

class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        # Create an LRUCache with capacity 2
        cache = LRUCache(2)
        cache.put(1, "A")  # Cache is {1: "A"}
        cache.put(2, "B")  # Cache is {1: "A", 2: "B"}
        self.assertEqual(cache.get(1), "A")  # Returns "A"
        cache.put(3, "C")  # Evicts key 2, Cache is {1: "A", 3: "C"}
        self.assertEqual(cache.get(2), -1)  # Returns -1 (not found)
        cache.put(4, "D")  # Evicts key 1, Cache is {3: "C", 4: "D"}
        self.assertEqual(cache.get(1), -1)  # Returns -1 (not found)
        self.assertEqual(cache.get(3), "C")  # Returns "C"
        self.assertEqual(cache.get(4), "D")  # Returns "D"

# Stress test for LRUCache
class StressTestLRUCache(unittest.TestCase):
    def test_stress_lru_cache(self):
        cache = LRUCache(1000)  # Create a cache with large capacity
        for i in range(2000):
            cache.put(i, str(i))  # Add 2000 items
        for i in range(1000):
            self.assertEqual(cache.get(i), str(i))  # First 1000 should be retrievable
        for i in range(1000, 2000):
            self.assertEqual(cache.get(i), -1)  # Last 1000 should not be retrievable

# Run the tests
if __name__ == '__main__':
    unittest.main()