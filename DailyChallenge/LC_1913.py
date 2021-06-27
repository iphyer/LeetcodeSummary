class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # 1stMax * 2ndMax - 1stMin * 2ndMin
        nums = sorted(nums)
        return nums[-1] * nums[-2] - nums[0] * nums[1] 
            
