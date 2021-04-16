class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [-1] * maxSize
        self.top = -1
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        if self.top < self.maxSize-1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top >= 0:
            self.top -= 1
            return self.stack[self.top+1]
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        tmp = 0
        count = 1
        while tmp <= self.top and count <= k:
            self.stack[tmp] += val
            count += 1
            tmp += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
