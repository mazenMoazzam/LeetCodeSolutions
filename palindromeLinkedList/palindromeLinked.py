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
            string += str(current.val)l
            current = current.next
        
        return string == string[::-1] 

#Time Complexity: O(n)
#Space complexity: O(n) due to string definition on line 12, can make constant space by modifying linkedlist by finding the middle element and compare the first half before middle element and second half after middle element
#and compare to see if they are the same, if they are, the linked list is a palindrome, otherwise, return false. 
