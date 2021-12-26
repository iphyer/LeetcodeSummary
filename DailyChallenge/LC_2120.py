class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = [0] * len(s)
        moves = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}
        for i in range(len(s)):
            curr_row, curr_col = startPos[0],  startPos[1]
            curr_step = 0
            for j in range(i, len(s)):
                tmp_row, tmp_col = curr_row + moves[s[j]][0], curr_col + moves[s[j]][1]
                if 0 <= tmp_row < n and 0 <= tmp_col < n:
                    curr_step += 1
                    curr_row, curr_col = tmp_row, tmp_col
                else:
                    break
            ans[i] = curr_step
        return ans
