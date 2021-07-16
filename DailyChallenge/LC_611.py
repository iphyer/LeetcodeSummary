class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        nums = sorted(nums)
        
        for p in range(2, len(nums)):
            p1, p2 = 0, p-1
            while p1 < p2:
                if (nums[p1] + nums[p2]) > nums[p]:
                    ans += (p2-p1)
                    p2 -= 1
                else:
                    p1 += 1
        return ans
        
        """
        res = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    tmpList = [nums[i], nums[j], nums[k]]
                    tmpList = sorted(tmpList)
                    #print(tmpList)
                    if tmpList[2] < (tmpList[0] + tmpList[1]):
                        res += 1
        return res
        """
                    
