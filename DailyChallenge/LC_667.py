class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1: return [i+1 for i in range(n)]
        
        res = [i for i in range(1, n - k)]
        
        for i in range(k+1):
            if i % 2 == 0:
                res.append(n-k+i//2)
            else:
                res.append(n-i//2)
        return res
