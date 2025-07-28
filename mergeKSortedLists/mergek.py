from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        dummy = ListNode(0)
        current = dummy

        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
            
        while heap:
            value, i, node = heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
