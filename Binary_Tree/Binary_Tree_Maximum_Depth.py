# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        depth = 0
        if root:
            return self.dfs(root, depth+1)
        return depth
    
    def dfs(self, node, depth):
        left_depth = right_depth = 0

        if node.left:
            left_depth = self.dfs(node.left, depth+1)
        
        if node.right:
            right_depth = self.dfs(node.right, depth+1)
        
        return max(left_depth, right_depth, depth)

