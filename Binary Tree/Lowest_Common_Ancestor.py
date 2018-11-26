# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.get_path(root, p, [])
        q_path = self.get_path(root, q, [])
        
        same_path = set(p_path) & set(q_path)

        if same_path:
            return same_path[-1]           
    

    def get_path(self, node, target, path):
        path.append(node.val)
        if  node.val != target:
            if not node.left and not node.right:
                return path.pop()
            
            if node.left:
                return get_path(node.left, target, path)

            if node.right:
                return get_path(node.right, target, path)
        else:
            return path
            





