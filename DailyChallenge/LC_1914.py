class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        for _ in range(m):
            res.append([0] * n)
        num_layers = min(m, n) // 2

        for i_layer in range(num_layers):
            w_m, w_n = m - 2* i_layer, n - 2*i_layer
            row = m - i_layer
            col = n - i_layer
            period = 2*w_m + 2*w_n - 4
            dis = k % period
            layer = []
            pos = []
            
            # get layer elements
            for i in range(i_layer, col):
                layer.append(grid[i_layer][i])
                pos.append((i_layer, i))
            for j in range(i_layer+1, row):
                layer.append(grid[j][i])
                pos.append((j, i))
            for p in range(i-1, i_layer-1, -1):
                layer.append(grid[j][p])
                pos.append((j, p))
            for q in range(j-1, i_layer, -1):
                layer.append(grid[q][p])
                pos.append((q, p))

            # Fill res
            count = 0
            while count <= period:
                r,c = pos[count%period]
                res[r][c] = layer[dis%period]
                dis += 1
                count += 1
        return res
