# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.path_sum_list = []
        if root:
            self.cal_path_sum(root, 0)
        if sum in self.path_sum_list:
            return True
        return False
    
    def cal_path_sum(self, root, sum):
        if root:
            sum += root.val
            if root.left:
                self.cal_path_sum(root.left, sum)
            
            if root.right:
                self.cal_path_sum(root.right, sum)
            
            if not root.left and not root.right:
                self.path_sum_list.append(sum)
