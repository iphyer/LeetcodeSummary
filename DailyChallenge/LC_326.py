class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res <= n:
            if res == n:
                return True
            else:
                res *= 3
        return False
        
# Another Solution

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 = 3^19 < 3^⌊19.56⌋ = 2^31
        return n > 0 and 1162261467 % n == 0
