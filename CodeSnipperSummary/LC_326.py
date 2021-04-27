class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 = 3^19 < 3^⌊19.56⌋ = 2^31
        return n > 0 and 1162261467 % n == 0
