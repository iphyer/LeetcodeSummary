class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 1
        count = 1
        prev = nums[0]
        
        while i < len(nums):
            if nums[i] == prev:
                count +=1
            else:
                prev = nums[i]
                count = 1
            
            if count > 1:
                del nums[i]
                i -= 1
            i += 1
            
        return len(nums)
            
            
            
