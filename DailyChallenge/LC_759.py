class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # pick each ele to be maximum ele
        # Then sliding windows
        res = 0
        for ind,num in enumerate(nums):
            # num itself is in or not
            if left <= num <= right:
                res += 1
                # sliding windows
                # p1, p2 in 
                #   in range 0~len(nums)-1
                #   nums(p1) < num
                #   nums(p2) <= num
                p1, p2 = ind-1, ind+1
                while p1 > -1 and nums[p1] < num:
                    p1 -= 1
                    res += 1

                while p2 < len(nums) and nums[p2] <= num:
                    p2 += 1
                    res += 1
                # Crossing num
                if p1+1 != ind and p2-1 != ind:
                    res += (ind-p1-1) * (p2-ind-1)
        return res
