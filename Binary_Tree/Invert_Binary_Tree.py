# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            new_node = TreeNode(root.val)

            if root.left:
                new_node.right = self.invertTree(root.left)
            
            if root.right:
                new_node.left = self.invertTree(root.right)
        
            return new_node
        
        return []
