class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        d = 0
        x = y = 0
        for op in instructions:
            if op == "G":
                x += dirs[d][0]
                y += dirs[d][1]
            elif op == "L":
                d = (d + 1) % 4
            else:
                d = (d - 1) % 4
            print(x,y,d) 
        return x == y == 0 or d != 0
