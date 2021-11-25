class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.dat = defaultdict(list)
        for ind,val in enumerate(arr):
            self.dat[val].append(ind)

    def query(self, left: int, right: int, value: int) -> int:
        # Not Found
        if value not in self.dat: return 0
        else:
            # Found
            # Not in left-right
            if self.dat[value][-1] < left or self.dat[value][0] > right:
                return 0
            else:
                # Found and in range
                # Binary search for L,R pointers
                l = bisect_left(self.dat[value], left)
                r = bisect_right(self.dat[value], right)
                return r-l
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
