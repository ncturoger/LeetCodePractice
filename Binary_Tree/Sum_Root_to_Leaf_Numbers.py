# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.nums = []
        if root:
            self.find_all_num(root, [])
        
        
        return sum(self.nums)
    

    def find_all_num(self, root, walked_nodes):
        walked_nodes = [node for node in walked_nodes]
        walked_nodes.append(root)

        if root.right:
            self.find_all_num(root.right, walked_nodes)

        if root.left:
            self.find_all_num(root.left, walked_nodes)


        if not root.right and not root.left:
            number = ""
            for node in walked_nodes:
                number += str(node.val)
            number + str(root.val)
            self.nums.append(int(number))


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.left = node_2
node_1.right = node_3

assert Solution().sumNumbers(node_1) == 25