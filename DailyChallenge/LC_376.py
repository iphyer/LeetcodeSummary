class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 1 
        if N == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return N
        
        up = 1
        down = 1
        
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                up = down + 1
            if nums[i] < nums[i-1]:
                down = up + 1

        return max(down, up)
