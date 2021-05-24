class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        res = [[1], [1,1]]
        currN = 2
        while numRows - 2 > 0:
            currN += 1
            currRow = [1]
            for i in range(len(res[-1])-1):
                currRow.append(res[-1][i] + res[-1][i+1])
            currRow.append(1)
            res.append(currRow)
            numRows -= 1
        return res
