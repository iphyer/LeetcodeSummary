 """
 
reversed order DP
 
 """

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # reversed order DP
        N = len(questions)
        dp = [0] * (N+1)
        
        for i in range(N-1, -1, -1):
            # not do question i
            dp[i] = dp[i+1]
            # do question i
            j = i + questions[i][1] + 1
            if j < N:
                dp[i] = max(dp[i+1], questions[i][0] + dp[j])
            else:
                dp[i] = max(dp[i+1], questions[i][0] )
        return dp[0]
      
      
 """
 
 ordered DP
 
 """

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i, q in enumerate(questions):
            f[i + 1] = max(f[i + 1], f[i])
            j = min(i + q[1] + 1, n)
            f[j] = max(f[j], f[i] + q[0])
        return f[n]
