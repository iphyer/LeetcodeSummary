class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0]
        ans = count
        for i in range(1, len(nums)):
            if nums[i] > prev:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
            prev = nums[i]
        return ans
