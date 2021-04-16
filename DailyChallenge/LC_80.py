class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        prev = nums[0]
        count = 1
        
        while ind < len(nums):
            # check if prev == current number
            if nums[ind] == prev: 
                count += 1
            else:
                prev = nums[ind]
                count = 1
            # duplicated,del value
            if count > 2: 
                del nums[ind]
                ind -= 1
            ind += 1

        return len(nums)
