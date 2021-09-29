class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # two pointers
        p1, p2 = 1, 0
        n = len(nums)
        
        while p1 < n and p2 < n:
            Flag = False
            # find odd mismatch
            while p1 < n:
                if nums[p1] % 2 == 0:
                    Flag = True
                    break
                else:
                    p1 += 2
                    
            # find even mismatch
            while p2 < n:
                if nums[p2] % 2 != 0:
                    break
                else:
                    p2 += 2
            # if mismatch found
            if Flag:
                nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums
