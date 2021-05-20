class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        
        First, the method of decreasing 1 instead of adding 1 for n-1 elements is brilliant. But, when I was doing the contest, I was dumb, so dumb to think outside the box. And this is how I tackled it using just math logic.
First, traverse the array, get the sum and the minimum value. If every element is equal, then min*(len) should equal to sum. This part is easy to understand. So, if they are not equal, what should we do? we should keep adding 1 to the array for k times until min*(len)==sum. Then we have:
len*(min+k)=sum+k*(len-1). ==> k=sum-min*len;
        
        
        http://buttercola.blogspot.com/2019/05/leetcode-453-minimum-moves-to-equal.html#:~:text=May%2023%2C%202019-,Leetcode%20453%3A%20Minimum%20Moves%20to%20Equal%20Array%20Elements,n%20%2D%201%20elements%20by%201.&text=Solution%3A,n%2D1%20elements%20is%20brilliant.
        
        """
        # len*(min+k)=sum+k*(len-1). ==> k=sum-min*len
        return sum(nums) - min(nums) * len(nums)
