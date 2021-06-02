class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        visited =[ [ 0 for _ in range(ncols) ] for _ in range(nrows) ]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        res = 0
        self.currArea = 1
        # DFS
        def DFS(r,c):
            for d in dirs:
                tmp_r, tmp_c = r+d[0], c+d[1]
                if 0 <= tmp_r < nrows and 0 <= tmp_c < ncols and grid[tmp_r][tmp_c] == 1 and not visited[tmp_r][tmp_c]:
                    self.currArea += 1
                    visited[tmp_r][tmp_c] = 1
                    DFS(tmp_r, tmp_c)
        
        for i in range(nrows):
            for j in range(ncols):
                if not visited[i][j]:
                    visited[i][j] = 1
                    if grid[i][j] == 1:
                        self.currArea = 1
                        DFS(i, j)
                        res = max(res, self.currArea)
        return res
                        
                    
