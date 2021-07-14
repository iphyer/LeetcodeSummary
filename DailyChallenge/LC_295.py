class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # small to large
        # pop large by multiplying -1
        self.Heap1 = []
        # large to small
        # pop small
        self.Heap2 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.Heap1, -num)
        heappush(self.Heap2, -heappop(self.Heap1))
        
        if len(self.Heap2) > len(self.Heap1):
            heappush(self.Heap1, -heappop(self.Heap2))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.Heap1) != len(self.Heap2):
            return -self.Heap1[0]
        else:
            return (self.Heap2[0]-self.Heap1[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
