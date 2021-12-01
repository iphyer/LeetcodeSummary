class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # dp[i]: the max value until house i
        dp = [0] * len(nums)
        N = len(nums)
        if N == 1: return nums[0]
        if N == 2: return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[N-1]
