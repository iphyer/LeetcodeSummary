class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        # calcualte same number index
        ind_dict = defaultdict(list)
        for ind, val in enumerate(arr):
            ind_dict[val].append(ind)
        
        # calculate prefix sum
        prefix_sum_dict = dict()
        curr_prefix_ind = dict()
        # loop to collect all intervals and calcualte it
        for i in range(len(arr)):
            if arr[i] not in prefix_sum_dict:
                # build prefix_sum array for arr[i]
                n = len(ind_dict[arr[i]])
                curr_prefix = [0] * n
                curr = 0
                for j in range(n):
                    curr += ind_dict[arr[i]][j]
                    curr_prefix[j] = curr
                # store results
                prefix_sum_dict[arr[i]] = curr_prefix
                curr_prefix_ind[arr[i]] = 0
            # prepare ans
            ans[i] = (2 * (curr_prefix_ind[arr[i]] + 1) - len(ind_dict[arr[i]])) * ind_dict[arr[i]][curr_prefix_ind[arr[i]]] + prefix_sum_dict[arr[i]][-1] - 2 * prefix_sum_dict[arr[i]][curr_prefix_ind[arr[i]]]
            curr_prefix_ind[arr[i]] += 1
                
        return ans
