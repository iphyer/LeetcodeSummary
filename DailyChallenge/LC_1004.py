class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, num_zeros, r = 0, 0, 0 
        ans = 0
        
        while r < len(nums):
            if nums[r] == 0: num_zeros += 1
            while num_zeros > k:
                # 1 1 1 0 0 1 1 1 1 1 0
                #         l           r           
                # move l to keep the same window
                if nums[l] == 0: num_zeros -= 1
                l += 1

            ans = max(ans, r-l+1)
            r += 1
        return ans
