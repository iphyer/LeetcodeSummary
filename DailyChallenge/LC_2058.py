# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # init
        if head: 
            p1 = head
            p2 = p1.next
        else: return [-1, -1]
        
        if p2: p3 = p2.next
        else: return [-1, -1]
            
        if not p3: return [-1, -1]
        
        ind = 1
        criticalPoints = []
        # loop all nodes
        while p3:
            if p1.val > p2.val and p3.val > p2.val:
                criticalPoints.append(ind)
            if p1.val < p2.val and p3.val < p2.val:
                criticalPoints.append(ind)
            # update nodes
            tmp3 = p3
            tmp2 = p2
            p3 = tmp3.next
            p2 = tmp3
            p1 = tmp2
            ind += 1
        # check criticalPoints to return
        if len(criticalPoints) < 2: return [-1, -1]
        else:
            maxD = criticalPoints[-1] - criticalPoints[0]
            minD = maxD
            for i in range(1, len(criticalPoints)):
                if criticalPoints[i] - criticalPoints[i-1] < minD:
                    minD = criticalPoints[i] - criticalPoints[i-1]
            return [minD, maxD]
            
