class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                if l == r : res += 2
                if l - 1 == r or l == r-1: res += 1
            else:
                l += nums[i]
                r -= nums[i]
        return res
