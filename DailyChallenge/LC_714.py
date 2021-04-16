class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # sold[i] selling at day i or do nothing
        # sold[i] = max( sold[i-1], hold[i-1] + prices[i] - fee)
        # hold[i] buying at day i or do nothing
        # hold[i] = max( hold[i-1], sold[i-1] - prices[i])
        N = len(prices)
        sold = [0] * N
        hold = [0] * N
        sold[0] = 0
        hold[0] = -prices[0]
        
        for i in range(1, N):
            sold[i] = max( sold[i-1], hold[i-1] + prices[i] - fee)
            hold[i] = max( hold[i-1], sold[i-1] - prices[i])
        return sold[N-1]
