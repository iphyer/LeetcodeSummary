class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= k:
                if stack[-k:] == [stack[-1]] * k:
                    del stack[-k:]
        return "".join(stack)
