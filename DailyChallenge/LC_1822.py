class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                res += 1
            else: pass
        if res % 2 == 0:
            return 1
        else:
            return -1
