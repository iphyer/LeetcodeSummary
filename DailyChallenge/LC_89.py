# i^(i>>1)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1<<n):
            res.append(i^(i>>1))
        return res
      
# Mirror

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res
