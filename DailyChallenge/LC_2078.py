"""

Solution 1

"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ind_colors = defaultdict(list)
        
        for ind,col in enumerate(colors):
            ind_colors[col].append(ind)
        
        cols = ind_colors.keys()
        
        res = -1
        
        for k1 in cols:
            for k2 in cols:
                if k1 != k2:
                    res = max(abs(ind_colors[k1][0] - ind_colors[k2][-1]),
                              abs(ind_colors[k2][0] - ind_colors[k1][-1]),
                              res)
        return res
        
        
 """

Solution 2

"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        j = len(colors) - 1
        
        
        # to the last
        while i < len(colors):
            if colors[i] == colors[len(colors)-1]:
                i += 1
            else:
                break
        
        # to the last
        while j >= 0:
            if colors[j] == colors[0]:
                j -= 1
            else:
                break
        
        return max(len(colors) - 1 - i, j)
