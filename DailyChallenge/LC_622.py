class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.total = 0
        self.head = 0
        self.tail = -1
        self.arr = [0] * k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail += 1
            if self.tail == self.capacity:
                self.tail = 0
            self.arr[self.tail] = value
            self.total += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.arr[self.head] = 0
            self.head += 1
            if self.head == self.capacity:
                self.head = 0
            self.total -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.tail]

    def isEmpty(self) -> bool:
        if self.total == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return self.capacity == self.total


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
