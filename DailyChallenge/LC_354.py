class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        N = len(envelopes)
        stack = []
        stack.append(envelopes[0][1])
        for i in range(1,N):
            if envelopes[i][1] > stack[-1]:
                stack.append(envelopes[i][1])
            else:
                ind = bisect.bisect_left(stack, envelopes[i][1])
                stack[ind] = envelopes[i][1]
        return len(stack)
        """
        # dp[i] means max number of envelopes can hold 
        # when i-th envelopes is the largest
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        """
