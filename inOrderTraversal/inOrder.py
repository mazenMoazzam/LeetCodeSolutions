# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorderWalker(node): 
            if node == None: 
                return []
            return inorderWalker(node.left) + [node.val] + inorderWalker(node.right)
        
        return inorderWalker(root)

  #depth first search used for this problem
