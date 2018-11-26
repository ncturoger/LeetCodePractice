# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        traverse_list = []
        check_list = [root]
        while (len(check_list) > 0):
            new_check_list = []
            value_list = []
            for node in check_list:
                if node:
                    if node.val:
                        value_list.append(node.val)
                    if node.left:
                        new_check_list.append(node.left)
                    if node.right:
                        new_check_list.append(node.right)
            traverse_list.append(value_list)
            check_list = new_check_list
        
        return traverse_list
