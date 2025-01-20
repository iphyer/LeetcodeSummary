# """
# 1265. Print Immutable Linked List in Reverse


# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # res = []
        # curr = head
        # while curr:
        #     res.append(curr.printValue())
        #     curr = curr.getNext()
        # print(res)
        # return [res[x] for x in range(len(res)-1, -1, -1)]

        '''
        # Recursion
        if head is not None:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
        '''

        # stack
        stack = []

        while head:
            stack.append(head)
            head = head.getNext()
        
        while stack:
            node = stack.pop()
            node.printValue()
