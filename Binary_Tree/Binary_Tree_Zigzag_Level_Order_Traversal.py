# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            result_list = []
            direct = 1
            check_list = [root]

            while check_list:
                traverse_list = []
                walk_list = []
                new_check_list = []
                for node in check_list:
                    if node:
                        traverse_list.append(node.val)
                        walk_list.append(node)

                result_list.append(traverse_list)
                while walk_list:
                    node = walk_list.pop()

                    if direct == 1:
                        if node.right:
                            new_check_list.append(node.right)
                        if node.left:
                            new_check_list.append(node.left)

                    elif direct == -1:
                        if node.left:
                            new_check_list.append(node.left) 
                        if node.right:
                            new_check_list.append(node.right)


                direct *= -1
                check_list = new_check_list
            return result_list
        else:
            return []
            
              


