class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        tmp = [edges[0][0], edges[0][1]]
        if edges[1][0] in tmp: return edges[1][0]
        else: return edges[1][1]
