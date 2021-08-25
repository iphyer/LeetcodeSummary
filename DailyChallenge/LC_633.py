class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        
        c1 = int(math.sqrt(c))
        
        for i in range(0, c1+1):
            b2 = c - i*i
            b = int(math.sqrt(b2))
            if b*b == b2:
                return True
        return False
        
