class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        flag = True
        if num < 0:
            flag = False
            num = abs(num)
        res = deque()
        while num:
            res.appendleft(str(num%7))
            num = num // 7
        if flag:
            return "".join(res)
        else:
            return "-"+"".join(res)
