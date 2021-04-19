class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] the # of conbinations to reach i
        # dp[i] = sum( dp[x] ) where x <= i
        # reference: https://www.cnblogs.com/grandyang/p/5705750.html
        dp = [0] * (target+1)
        dp[0] = 1 # base case
        nums = sorted(nums)
        
        for i in range(1, len(dp)):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
                else:
                    break
        return dp[-1]
