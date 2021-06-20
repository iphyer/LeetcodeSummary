class Solution:
    def largestOddNumber(self, num: str) -> str:
        N = len(num)
        Flag = False
        for i in range(N-1, -1, -1):
            if int(num[i]) % 2 == 1:
                Flag = True
                break
        if Flag:
            return num[:i+1]
        else:
            return ""
