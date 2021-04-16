class SnapshotArray:

    def __init__(self, length: int):
        self.array = defaultdict(defaultdict)
        self.snapID = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        if index < self.length:
            self.array[self.snapID][index] = val

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id >= 0:
            if index in self.array[snap_id]:
                return self.array[snap_id][index]
            snap_id -= 1
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
