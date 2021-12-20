class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        prev = 0
        for sp in spaces:
            ans += s[prev:sp] + " "
            prev = sp
        return ans + s[prev:]
