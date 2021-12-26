class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        
        for p in points:
            heapq.heappush(heap, (-1 * ((p[0])**2+(p[1])**2), p ))
            if len(heap) > k: heapq.heappop(heap)

                
        return [i[1] for i in heap]
