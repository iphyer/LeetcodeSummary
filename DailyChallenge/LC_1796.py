class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for ch in s:
            if ch.isdigit():
                res.add(int(ch))
        res = sorted([d for d in res])
        print(res)
        if len(res) >= 2:
            return res[-2]
        else:
            return -1
