# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        self.traverse_list = []
        self.preoderTraverser(root, self.traverse_list)
        return self.traverse_list
    
    def preoderTraverser(self, root, traverse_list):
        if root:
            traverse_list.append(root.val)
            if root.left:
                self.preoderTraverser(root.left, traverse_list)
        
            if root.right:
                self.preoderTraverser(root.right, traverse_list)
            