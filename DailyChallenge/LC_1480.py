class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        tmp = 0
        for num in nums:
            tmp += num
            res.append(tmp)
        return res
