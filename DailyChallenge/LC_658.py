class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
      
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        
        if x > arr[-1]:
            return arr[k:]
        
        # in the array range
        # remove leftmost or rightmost based on distance to x
        while arr and len(arr) != k:
            if abs(x-arr[0]) <= abs(arr[-1]-x):
                arr.remove(arr[-1])
            else:
                arr.remove(arr[0])
        return arr
