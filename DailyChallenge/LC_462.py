class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        This problem is deceptive in its simplicity. Ultimately, the value to which you want to set each element equal is the median of the sorted nums array. To come to this realization, we have to first think about the nature of the problem.

Let's consider a possible scenario in which we've decided that our target value is x which would take ans number of moves to complete. What would happen to ans if we increased x by 1? If we did, each element that is below the new x would have to spend another move to get up to x, but every element that is above the new x would have to spend one less move to get down to x.

This means that x should naturally move up if there are more elements above x than below. It also means the inverse, that x should move down if there are more elements below x than above. The natural outcome of this is that x will settle at a spot where there are the same number of elements on either side, which is the median value of nums.

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/1217591/JS-Python-Java-C%2B%2B-or-Easy-Mathematical-Solution-w-Explanation
   
        """
        median = sorted(nums)[len(nums)//2]
        res = 0
        for num in nums:
            res += abs(num-median)
        return res
