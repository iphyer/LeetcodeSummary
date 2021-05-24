class Solution:
    def isUgly(self, n: int) -> bool:
        factor = [2, 3, 5]
        
        if n == 0: return False
        if n < 0: return False
        
        while n % factor[0] == 0:
            n /= factor[0]
        
        while n % factor[1] == 0:
            n /= factor[1]
        
        while n % factor[2] == 0:
            n /= factor[2]
        
        return n == 1
