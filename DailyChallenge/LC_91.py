class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: number of ways to decode from 0 to i
        # s[i] ,s[i-1]s[i]
        # s[i] not valid, s[i-1]s[i] not valid == > 0.      e.g. "1000"
        # s[i] is  valid, s[i-1]s[i] not valid == > dp[i-1] e.g. "101" 
        # s[i] not valid, s[i-1]s[i] is  valid == > dp[i-2] e.g. "110"
        # s[i] is  valid, s[i-1]s[i] is  valid == > dp[i-1] + dp[i-2]
        
        if len(s) == 0: return 0
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        
        # at least str of length 2

        def isValid(*args):
            if len(args) == 1:
                return s[args[0]] != "0"
            if len(args) == 2:
                tmp = int(s[args[0]])* 10 + int(s[args[1]])
                return (tmp >= 10) and (tmp <= 26) 
        
        # init dp variable 
        dp_i_2 = 1
        dp_i_1 = 1
        dp_i = 0
        
        for i in range(1, len(s)):
            if (isValid(i) and isValid(i-1, i)):
                dp_i = dp_i_2 + dp_i_1
            if (isValid(i) and not isValid(i-1, i)):
                dp_i = dp_i_1
            if (not isValid(i) and isValid(i-1, i)):
                dp_i = dp_i_2
            if (not isValid(i) and not isValid(i-1, i)):
                return 0

            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        
        return dp_i
