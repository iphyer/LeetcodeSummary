class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res <= n:
            if res == n:
                return True
            else:
                res *= 3
        return False
        
