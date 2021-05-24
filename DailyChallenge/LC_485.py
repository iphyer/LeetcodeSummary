class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = currOnes = 0
        for num in nums:
            if num == 1:
                currOnes += 1
                res = max(res, currOnes)
            else:
                currOnes = 0
            prev = num
        return res
