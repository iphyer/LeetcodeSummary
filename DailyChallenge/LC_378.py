class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        heap_min = [(matrix[i][0], i, 0 ) for i in range(n)]
        heapq.heapify(heap_min)
        
        for _ in range(k-1):
            # pop current min in heap
            _, row, col = heapq.heappop(heap_min)
            if col + 1 < n:
                heapq.heappush(heap_min, (matrix[row][col+1], row, col+1))
        return heapq.heappop(heap_min)[0]
        
        
  # Another Solution
  
  class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
