class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrows, ncols = len(matrix), len(matrix[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        mem = dict()
        
        def DFS(r, c):
            if (r,c) in mem: return mem[(r,c)]
            
            currLen = 1
            for i,j in dirs:
                tmp_r, tmp_c = r+i, c+j
                if 0 <= tmp_r < nrows and 0 <= tmp_c < ncols and matrix[tmp_r][tmp_c] > matrix[r][c]:
                    currLen = max(currLen, DFS(tmp_r, tmp_c)+1)
            mem[(r,c)] = currLen
            
            return currLen
        
        maxLen = -1
        for i in range(nrows):
            for j in range(ncols):
                maxLen = max(maxLen, DFS(i,j))
        return maxLen
