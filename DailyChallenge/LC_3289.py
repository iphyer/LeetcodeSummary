class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ss = set()
        res = []
        for n in nums:
            if n not in ss:
                ss.add(n)
            else:
                res.append(n)
        return res
