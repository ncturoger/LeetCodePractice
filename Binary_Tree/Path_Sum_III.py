# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = 0
        if root:
            check_list = [root]
            while check_list:
                new_list = []
                for node in check_list:
                    count += self.bfs_sum(node, sum)
                    if node.left:
                        new_list.append(node.left)

                    if node.right:
                        new_list.append(node.right)

                check_list = new_list
        
        return count

    def bfs_sum(self, root, sum):
        count = 0
        if root:
            check_list = [root]
            val_list = [root.val]
            while check_list:
                new_check_list = []
                new_val_list = []
                for idx, node in enumerate(check_list):
                    if val_list[idx] == sum:
                        count += 1
                    if node.left:
                        new_check_list.append(node.left)
                        new_val_list.append(val_list[idx] + node.left.val)

                    if node.right:
                        new_check_list.append(node.right)
                        new_val_list.append(val_list[idx] + node.right.val)

                check_list = new_check_list
                val_list = new_val_list
        return count


    

