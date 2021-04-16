class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * len(arr)
        pos_val_mapping = dict()
        for ind, val in enumerate(arr):
            pos_val_mapping[val] = ind
        # loop through each val and find its child
        # dp[u] = dp[x] * dp[u//x] if u//x in arr and x in arr
        for ind,val in enumerate(arr):
            for i in range(ind):
                if val % arr[i] == 0:
                    # arr[i] is factor of val
                    if val / arr[i]  in arr:
                        dp[ind] += dp[ i ] * dp[ pos_val_mapping[val / arr[i] ] ]
        return sum(dp) % (10**9 + 7)
