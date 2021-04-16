class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        self.position = sorted(position)
        low, high = 0, self.position[-1] - self.position[0]
        while low <= high:
            mid = (high+low) // 2
            if self.check(self.position, m, mid):
                low = mid + 1
            else:
                high = mid - 1

        if self.check(self.position, m, high):
            return high
        else:
            return high - 1

    def check(self, pos, num, gap):
        count = 1
        prev = pos[0]
        for curr in pos:
            if (curr - prev) >= gap:
                count += 1
                prev = curr
            if count == num: return True
        return False
