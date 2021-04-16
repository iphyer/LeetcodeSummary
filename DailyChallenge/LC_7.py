class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0: 
            Flag = -1
            x = abs(x)
        else: 
            Flag = 1
        while x:
            #pop operation:
            pop = x % 10
            x //= 10

            #push operation:
            temp = rev * 10 + pop
            rev = temp
        res = rev * Flag
        if res < - 2**31: return 0
        elif res > 2**31-1: return 0
        return res
