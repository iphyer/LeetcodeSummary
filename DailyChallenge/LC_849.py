class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = -1
        N = len(seats)
        
        prev_one = -1
        while prev_one < N:
            prev_one += 1
            if seats[prev_one] == 1:
                break
        if prev_one != 0:
            # put Alex in 0
            ans = prev_one
        
        curr_one = prev_one+1
        Flag_second_one = False
        while curr_one < N:
            if seats[curr_one] == 1:
                Flag_second_one = True
                ans = max(ans, (curr_one-prev_one)//2)
                prev_one = curr_one
            curr_one += 1
        
        if seats[N-1] != 1:
            # put Alex in N-1
            ans = max(ans, N-1 - prev_one)
        
        if not Flag_second_one: # [1, 0, 0, 0]
            ans = max(ans, prev_one, N-1-prev_one)
            
        return ans
            
