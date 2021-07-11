class Solution:
    def countTriples(self, n: int) -> int:
        sqr_dict = defaultdict(int)
        for num in range(n):
            sqr_dict[(num+1)**2] = num

        res = set()
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i!= j and (i**2 + j**2) in sqr_dict and (i,j) not in res:
                    res.add((i,j))
        return len(res)
        
