class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        nrows = len(grid2)
        ncols = len(grid2[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.path = []
        # grid1 + grid2 and only search for 2
        # Then in grid2 search if find any island has 1 or 0 is wrong

        for i in range(nrows):
            for j in range(ncols):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    grid2[i][j] = 2
        print(grid2)
        # DFS
        visited = []
        for _ in range(nrows):
            tmp = []
            for _ in range(ncols):
                tmp.append(0)
            visited.append(tmp)

        def DFS(r, c):
            visited[r][c] = 1
            self.path.append(grid2[r][c])
            for d in directions:
                tmp_r, tmp_c = r+d[0], c+d[1]
                if -1 < tmp_r < nrows and -1 < tmp_c < ncols and not visited[tmp_r][tmp_c] and grid2[tmp_r][tmp_c]: 
                    DFS(tmp_r, tmp_c)

        for i in range(nrows):
            for j in range(ncols):
                if not visited[i][j] and grid2[i][j] == 2:
                    self.path = []
                    DFS(i, j)
                    # print(self.path)
                    if not (1 in self.path):
                        res += 1

        return res
