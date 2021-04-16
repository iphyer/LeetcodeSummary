class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # edge cases
        if n == 1: return 1
        if k == 1: return n
        # general cases
        circle = [i for i in range(1,n+1)]
        start = 0
        while len(circle) > 1:
            start = (start + k -1) % len(circle)
            #print(start)
            del circle[start]
        return circle[0]
