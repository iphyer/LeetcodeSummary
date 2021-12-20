class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        min_diff = float('inf')
        
        # sorted arr
        arr = sorted(arr)

        # in sorted arr, the mini abs diff
        # is only possible for adj elements
        for i in range(len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            if curr_diff < min_diff:
                ans = []
                ans.append([arr[i], arr[i+1]])
                min_diff = curr_diff
            elif curr_diff == min_diff:
                ans.append([arr[i], arr[i+1]])
            else:
                pass
        return ans
