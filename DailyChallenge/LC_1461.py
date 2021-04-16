class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sub_s = set()
        for i in range(0, len(s) - k + 1):
            sub_s.add(s[i:i+k])
        return True if len(sub_s) == 2**k else False
