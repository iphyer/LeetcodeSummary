class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        F0 = 0
        F1 = 1
        while n-1 > 0:
            tmp = F0 + F1
            F0 = F1
            F1 = tmp
            n -= 1
        return F1
