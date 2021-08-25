class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                # Check the column
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)

        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # Check Row
        for i in range(N):
            num_used = set()
            for j in range(N):
                if board[i][j] != '.' and board[i][j] not in num_used:
                    num_used.add(board[i][j])
                elif board[i][j] != '.' :
                    return False
                else: pass
        # Check Col
        for j in range(N):
            num_used = set()
            for i in range(N):
                if board[i][j] != '.' and board[i][j] not in num_used:
                    num_used.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                else: pass

        # Check SubBoxes
        neighbours = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1), (0, 0), (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        for subbox_i in range(N):
            center_row= 1 + 3 * (subbox_i//3)
            center_col = 1 + 3 * (subbox_i%3)
            num_used = set()
            for vec in neighbours:
                i,j = center_row + vec[0], center_col + vec[1]
                if board[i][j] != '.' and board[i][j] not in num_used:
                    num_used.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                else: pass
        return True
        
