class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen_op = set()
        num_op = 1
        seed = deque([start])
        
        while seed:
            curr_N = len(seed)
            while curr_N > 0:
                curr = seed.popleft()
                # Loop all number in nums
                for num in nums:
                    for tmp in (curr+num, curr-num, curr^num):
                        if tmp == goal: return num_op
                        if tmp not in seen_op and 0 <= tmp <= 1000:
                            seen_op.add(tmp)
                            seed.append(tmp)
                curr_N -= 1
            num_op += 1
        return -1
