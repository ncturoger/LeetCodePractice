# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_count = 0
        if not root:
            return 0
        check_list = [root]
        while check_list:
            new_check_list = []
            for node in check_list:
                node_count += 1
                if node.left:
                    new_check_list.append(node.left)
                
                if node.right:
                    new_check_list.append(node.right)
                
            check_list = new_check_list
        
        return node_count
