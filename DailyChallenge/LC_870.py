class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        B_ind_val = defaultdict(list)
        for ind,val in enumerate(B):
            B_ind_val[val].append(ind)
        ans = [-1] * len(A)
        sortedB = sorted(B)
        i, j = 0, 0
        remaining_index_A = []
        # pair smallest A with smallest B if possibe
        # greedy
        while i < len(A):
            if sortedA[i] > sortedB[j]:
                B_ind = B_ind_val[sortedB[j]].pop()
                ans[B_ind] = sortedA[i]
                i += 1
                j += 1
            else:
                remaining_index_A.append(i)
                i += 1
        # complete unpaired A
        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = sortedA[remaining_index_A.pop()]
        return ans
