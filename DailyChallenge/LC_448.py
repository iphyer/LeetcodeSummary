class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        # mark number occurance with negative values
        for num in nums:
            curr = nums[abs(num) - 1]
            if curr > 0: nums[abs(num) - 1] *= -1
        # find non-showing interges
        for ind,num in enumerate(nums):
            if num > 0: res.append(ind+1)

        return res        
