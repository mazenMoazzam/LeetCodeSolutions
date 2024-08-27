# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
      #simple problem where we include three cases to account for if two trees are the same, if both nodes are none and they equal the same value, if neither is true, we return false and recursively
      #traverse the tree. 
        if p == None and q == None: 
            return True
        
        if p == None or q == None: 
            return False

        if p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

  #Time complexity: O(N) where N represents the number of nodes in the tree in the smaller of the two trees.
  #Space complexity: O(H) where H represents the height of the tree, this space is used for the recursion stack. 
