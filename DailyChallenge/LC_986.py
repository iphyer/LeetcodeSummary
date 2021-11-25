class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # intervals is pairwise disjoint and in sorted order.
        p1 = p2 = 0
        res = []
        
        while p1 < len(firstList) and p2 < len(secondList):
            # check larger startpoint and smaller endpoint
            start = max(firstList[p1][0], secondList[p2][0])
            end   = min(firstList[p1][1], secondList[p2][1])
            
            if start <= end:
                res.append([start, end])
                

            # remove smallest end of List1 and List2
            # since no other intervals can match it
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
                
        return res
