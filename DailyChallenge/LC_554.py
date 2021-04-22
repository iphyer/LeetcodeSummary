class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = defaultdict(int)
        n = len(wall)
        ending = sum(wall[0])
        
        for row in wall:
            c0 = 0
            for c in row:
                ind = c0 + c
                if ind != ending: freq[ind] += 1
                c0 = ind

        if not freq:
            return n
        else:
            return n - max(freq.values())
