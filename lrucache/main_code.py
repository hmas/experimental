class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1  # Key not found

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.capacity:
            # Remove the least recently used item
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# Unit tests
import unittest

class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)  # returns 1
        cache.put(3, 3)  # evicts key 2
        self.assertEqual(cache.get(2), -1)  # returns -1 (not found)
        cache.put(4, 4)  # evicts key 1
        self.assertEqual(cache.get(1), -1)  # returns -1 (not found)
        self.assertEqual(cache.get(3), 3)  # returns 3
        self.assertEqual(cache.get(4), 4)  # returns 4

    def test_stress_test(self):
        cache = LRUCache(100)
        for i in range(200):
            cache.put(i, i)
        for i in range(100, 200):
            self.assertEqual(cache.get(i), i)
        for i in range(100):
            self.assertEqual(cache.get(i), -1)  # should be evicted

if __name__ == '__main__':
    unittest.main()