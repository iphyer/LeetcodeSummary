class Solution:
    def totalMoney(self, n: int) -> int:
        n_week = n // 7
        if n_week > 0:
            res = (6 * n_week + (n_week + 1) * n_week) * 7 // 2
            remaining_week_end = n_week + (n - 7 * n_week)
            remaining_week_start = n_week + 1
            res += ((remaining_week_start + remaining_week_end) * (n - 7 * n_week) // 2)
            return res
        else:
            # first week
            return ((1+n) * n)//2
