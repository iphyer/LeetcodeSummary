class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # edge cases
        if maxDoubles == 0: return target-1
        if target == 1: return 0
        
        ans = 0
        
        while target != 1 and maxDoubles > 0:
            if target % 2 != 0:
                ans += 1
            target = target // 2
            ans += 1
            maxDoubles -= 1
        
        if target == 1: return ans
        else:
            return ans + target - 1
