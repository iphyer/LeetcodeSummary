class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1: return 1
        
        prev = s[0]
        power = 1
        ans = power
        for i in range(1, len(s)):
            if s[i] == prev:
                power += 1
                ans = max(power, ans)
            else:
                power = 1
            prev = s[i]
        return ans
