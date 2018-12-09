# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            mid = root.val
            if root.left:
                if not self.validate_BST(root.left, mid, None):
                    return False
            
            if root.right:
                if not self.validate_BST(root.right, None, mid):
                    return False
            
            return True
        

        else:
            return True

    

    def validate_BST(self, node, upbound, lowbound):
        mid = node.val

        if upbound is not None and lowbound is not None:
            if mid >= upbound or mid <= lowbound:
                return False
        
        elif upbound is not None:
            if mid >= upbound:
                return False
        
        elif lowbound is not None:
            if mid <= lowbound:
                return False

        
        if node.left:
            if not self.validate_BST(node.left, mid, lowbound):
                return False

        if node.right:
            if not self.validate_BST(node.right, upbound, mid):
                return False
        
        return True


node_1 = TreeNode(5)
node_2 = TreeNode(1)
node_3 = TreeNode(4)
node_4 = TreeNode(3)
node_5 = TreeNode(6)

node_1.left = node_2
node_1.right = node_3
node_3.left = node_4
node_3.right = node_5

assert Solution().isValidBST(node_1) == False

node_6 = TreeNode(3)
node_7 = TreeNode(30)
node_6.right = node_7
node_8 = TreeNode(10)
node_7.left = node_8
node_9 = TreeNode(15)
node_8.right = node_9
node_10 = TreeNode(45)
node_9.right = node_10

assert Solution().isValidBST(node_6) == False


node_11 = TreeNode(0)
node_12 = TreeNode(-1)
node_11.right = node_12

assert Solution().isValidBST(node_11) == False