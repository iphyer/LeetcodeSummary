class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] minimum number of coins to rearch i
        # dp[i] = min( dp[i-c] ) + 1 where c is from coins
        
        dp = [float('inf')] * ( amount+1 )
        dp[0] = 0
        for coin in coins:
            for val in range(coin, amount+1):
                dp[val] = min(dp[val], dp[val-coin]+1)
                print(dp) # coins = [1,2,5], amount = 11
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
