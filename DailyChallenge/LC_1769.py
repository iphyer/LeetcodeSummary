class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        res = []
        n = len(boxes)
        for i in range(n):
            tmp_sum = 0
            for j in range(n):
                if boxes[j]:
                    tmp_sum += (abs(j-i) * int(boxes[j]))
            res.append(tmp_sum)
        return res
        """
        # Reference: https://www.youtube.com/watch?v=XrOc63_GSsY
        n = len(boxes)
        # First Loop to get LeftMoves
        #   LeftMoves[i] =  LeftMoves[i-1] +  Left[i] * 1
        LeftMoves = [0] * n
        Left = int(boxes[0])
        for i in range(1, n):
            LeftMoves[i] =  LeftMoves[i-1] +  Left * 1
            Left += int(boxes[i])
        # Second Loop to get RightMoves
        #   RightMoves[i] = RightMoves[i+1] + Right[i] * 1
        RightMoves = [0] * n
        Right = int(boxes[n-1])
        for i in range(n-2, -1, -1):
            RightMoves[i] = RightMoves[i+1] + Right * 1
            Right += int(boxes[i])
        # Combine to get all moves
        res = []
        for i in range(0,n):
            res.append( LeftMoves[i] + RightMoves[i] )
        return res
