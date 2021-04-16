class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "": return 0
        # if alread palindrome, directly remove
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return 2
        return 1
