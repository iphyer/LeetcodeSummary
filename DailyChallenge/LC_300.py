"""

Bisect for Smart Building LIS

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
      
"""

DP Soultion

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS ends at nums[i]
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(0, i):
                # if nums[i] > nums[j] = > dp[i] = dp[j]+1
                # else: == > dp[i]
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)
