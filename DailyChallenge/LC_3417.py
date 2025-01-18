# LC 3417 Zigzag Grid Traversal With Skip

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        curr_x, curr_y = 0, 0
        len_y, len_x = len(grid), len(grid[0])
        res = list()
        direction = 1

        while curr_x < len_x and curr_y < len_y:
            res.append(grid[curr_y][curr_x])
            curr_x = curr_x + direction * 2
            while curr_x < len_x and curr_x >= 0: 
                res.append(grid[curr_y][curr_x])
                curr_x = curr_x + direction * 2
            curr_y += 1
            direction *= -1
            if curr_x == -2: curr_x = 1
            if curr_x == len_x + 1: curr_x = len_x - 2
            if curr_x == -1: curr_x = 0
            if curr_x == len_x: curr_x = len_x -1
            

        return res


            
# A more elegent solution 
# using i % 2 and the iteration to control order and reversed order of list

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(grid):
            res += r[::-1] if i % 2 else r
        return res[::2]
