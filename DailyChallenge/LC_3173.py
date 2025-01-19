# 3173. Bitwise OR of Adjacent Elements

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        curr = 1
        res = []
        while curr < len(nums):
            res.append(nums[curr]|nums[curr-1])
            curr += 1
        return res
