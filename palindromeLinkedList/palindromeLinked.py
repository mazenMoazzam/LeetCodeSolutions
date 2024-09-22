# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string = ""

        current = head

        while current != None:
            string += str(current.val)
            current = current.next
        
        return string == string[::-1]

