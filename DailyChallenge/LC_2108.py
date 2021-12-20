class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(w):
            # two pointers
            l, r = 0, len(w)-1
            while l < r:
                if w[l] == w[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        for w in words:
            if isPalindrome(w):
                #print(w)
                return w
        # not found
        return ""
