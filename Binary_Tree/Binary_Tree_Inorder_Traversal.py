# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        self.traverse_list = []
        self.inorderTraverser(root, self.traverse_list)
        return self.traverse_list
    
    def inorderTraverser(self, root, traverse_list):
        if root:
            if root.left:
                self.inorderTraverser(root.left, traverse_list)
            
            traverse_list.append(root.val)
        
            if root.right:
                self.inorderTraverser(root.right, traverse_list)