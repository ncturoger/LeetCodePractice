# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        self.traverse_list = []
        self.postorderTraverser(root, self.traverse_list)
        return self.traverse_list
    
    def postorderTraverser(self, root, traverse_list):
        if root:
            if root.left:
                self.postorderTraverser(root.left, traverse_list)
        
            if root.right:
                self.postorderTraverser(root.right, traverse_list)
            
            traverse_list.append(root.val)
        