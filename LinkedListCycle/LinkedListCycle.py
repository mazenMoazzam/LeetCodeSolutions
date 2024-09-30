# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        visitedNodes = set()
        current = head

        while current != None:
            if current in visitedNodes:
                return True
            visitedNodes.add(current)
            current = current.next  

        return False (previous solution of problem using set to store the visited nodes, if the current node is in the set, then it is a cycle and we would return true.
        '''
        if head is None or head.next is None:
            return False
        
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False
#I have two solutions for this problem, while the commented out one runs in linear time, the second one is more memory and time efficient. First approach involves using a set as a data structure, traverse the LL
#and add it to the set, if current is in the set, that means it indicates a cycle, which we return true, end of while loop will return false as it indicates a no cycle. Second solution involves the two-pointer
#algorithm, only intialized two variables which start at the head, the fast pointer will always be ahead of the slow, if both are equal in value, return true as this represents a cycle. Runtime: O(n) Space complexity: O(1). 
