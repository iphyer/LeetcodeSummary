class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 1: return nums.pop()
        if len(nums) == 2: return max(nums)
        
        N = 2
        while N > 0:
            val = max(nums)
            nums.remove(val)
            N -= 1
        return max(nums)
