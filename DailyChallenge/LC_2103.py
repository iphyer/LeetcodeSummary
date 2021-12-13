class Solution:
    def countPoints(self, rings: str) -> int:
        rings_rod = defaultdict(set)
        i = 0
        while i < len(rings) - 1:
            rings_rod[rings[i+1]].add(rings[i])
            i += 2
        ans = 0
        for key in rings_rod.keys():
            if len(rings_rod[key]) == 3: ans += 1
        return ans
