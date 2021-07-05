class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[i,j]
        # j is from CharIndDict,{'a':0, 'e':1. 'i':2, 'o':3, 'u':4}
        # i is the length of new string
        # dp[i,j] using Char_j as ending with length i permutation numbers
        """
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        
        So each sting ending with 
        
        'a' is from: 'e', 'i', 'u'
        'e' is from: 'a', 'i' 
        'i' is from: 'e', 'o'
        'o' is from: 'i'
        'u' is from: 'o', 'i'
        """
        # edge case
        if n == 1: return 5
        
        # {'a':0, 'e':1. 'i':2, 'o':3, 'u':4}
        dp0 = [1] * 5
        dp1 = [0] * 5
        mod = 10**9 + 7
        while n-1>0:
            for i in range(5):
                if i == 0: # 'a' is from: 'e', 'i', 'u'
                    dp1[0] = (dp0[1] + dp0[2] + dp0[4]) % mod
                elif i == 1: # 'e' is from: 'a', 'i' 
                    dp1[1] = (dp0[0] + dp0[2]) % mod
                elif i == 2: #'i' is from: 'e', 'o'
                    dp1[2] = (dp0[1] + dp0[3]) % mod
                elif i == 3: # 'o' is from: 'i'
                    dp1[3] = dp0[2] % mod
                else: #'u' is from: 'o', 'i'
                    dp1[4] = (dp0[3] + dp0[2]) % mod
            n -= 1
            # deep copy
            for i in range(5): dp0[i] = dp1[i]
        return sum(dp0)%mod
                
            
            
