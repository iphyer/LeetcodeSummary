class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1: return min(triangle[0])
        
        row_curr = triangle[n-1]
        
        for row in range(n-2, -1, -1):
            row_up = triangle[row]
            for ind in range(len(row_up)):
                row_up[ind] = min(row_curr[ind] +  triangle[row][ind], 
                                  row_curr[ind+1] + triangle[row][ind])
            row_curr = row_up
        return row_up[0]
