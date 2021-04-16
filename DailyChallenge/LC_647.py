class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # single char
            res += 1
            # odd substring
            l, r = i-1, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
            # even substring
            l,r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break
        return res

    """
    Another smarter solution to find the mid point
    
    Using // and % to find the middle point
    
            left = mid // 2
            right = left + mid % 2
    
    """

    class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        l = len(s)
        for mid in range(l * 2 - 1):
            left = mid // 2
            right = left + mid % 2
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
