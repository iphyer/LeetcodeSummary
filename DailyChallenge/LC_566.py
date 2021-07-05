class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nrows, ncols = len(mat), len(mat[0])
        if nrows * ncols != r*c: return mat
        
        res = []
        for i in range(r):
            res.append([0] * c)
        
        p = 0
        q = 0
        for i in range(nrows):
            for j in range(ncols):
                if q == c:
                    q = 0
                    p += 1
                res[p][q] = mat[i][j]
                q += 1
        return res
