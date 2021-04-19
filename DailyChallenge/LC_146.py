from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = OrderedDict()


    def get(self, key: int) -> int:
        if key in self.LRU:
            val = self.LRU[key]
            del self.LRU[key]
            self.LRU[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            del self.LRU[key]
            self.LRU[key] = value
        else:
            self.LRU[key] = value
            if len(self.LRU) > self.capacity:
                self.LRU.popitem(last=False)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
