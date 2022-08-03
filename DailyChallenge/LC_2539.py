class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # node1 == > list of rearchable nodes with steps, l1
        # detect cycles
        # node2 == > list of rearchable nodes with steps, l2
        # intercect of l1 and l2
        #   loop reachable nodes to find distance
        # return min( max(s1, s2) )  
        
        l1 = defaultdict(int)
        curr = node1
        step = 0
        while curr != -1 and curr not in l1:
            l1[curr] = step
            curr = edges[curr]
            step += 1

        l2 = defaultdict(int)
        curr = node2
        step = 0
        while curr != -1 and curr not in l2:
            l2[curr] = step
            curr = edges[curr]
            step += 1

        res = float('inf')
        res_index = -1
        for e1 in l1:
            if e1 in l2:
                if max(l1[e1], l2[e1]) < res:
                    res = max(l1[e1], l2[e1])
                    res_index = e1
                if max(l1[e1], l2[e1]) == res:
                    res_index = min(e1, res_index)
        return res_index
    
# tc : l1: O(n), l2: O(n), find res: O(n)
# O(n)
# SC: O(n)
