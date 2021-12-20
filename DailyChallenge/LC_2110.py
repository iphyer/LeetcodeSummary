class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 0
        
        while l <= r and r < len(prices):
            while r + 1 < len(prices) and prices[r+1] + 1 == prices[r]:
                r += 1
            ans += ((r-l+1) * (r-l+2) // 2)
            l = r+1
            r = l
        return ans
