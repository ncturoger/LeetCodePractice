# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """ 

        if t1 and t2:
            new_node = TreeNode(t1.val + t2.val)

            if t1.left and t2.left:
                new_node.left = self.mergeTrees(t1.left, t2.left)
            
            elif t1.left and not t2.left:
                new_node.left = self.mergeTrees(t1.left, None)

            elif not t1.left and t2.left:
                new_node.left = self.mergeTrees(None, t2.left)
            
            if t1.right and t2.right:
                new_node.right = self.mergeTrees(t1.right, t2.right)
            
            elif t1.right and not t2.right:
                new_node.right = self.mergeTrees(t1.right, None)

            elif not t1.right and t2.right:
                new_node.right = self.mergeTrees(None, t2.right)


        if t1 and not t2:
            new_node = t1
        
        if t2 and not t1:
            new_node = t2
        
        if not t1 and not t2:
            return None

        return new_node



    def traverseMerge(self, t1, t2):
        if t1 and t2:
            new_node = TreeNode(t1.val + t2.val)

            if t1.left and t2.left:
                new_node.left = self.traverseMerge(t1.left, t2.left)
            
            elif t1.left and not t2.left:
                new_node.left = self.traverseMerge(t1.left, None)
            
            if t1.right and t2.right:
                new_node.right = self.traverseMerge(t1.right, t2.right)
            
            elif t1.right and not t2.right:
                new_node.right = self.traverseMerge(t1.right, None)


        if t1 and not t2:
            new_node = t1
        
        if t2 and not t1:
            new_node = t2

































    def traverseMerge_1(self, t1, t2, last_node, direct):
        if t1 and t2:
            t1.val += t2.val

        elif t1 and not t2:
            t1.val = t1.val

        elif not t1 and t2:
            new_node = TreeNode(t2.val)
            if last_node:
                if direct:
                    last_node.right = new_node
                else:
                    last_node.left = new_node


        if t1.left and not t2.left:
            self.traverseMerge(t1.left, None, t1, 0)

        elif t1.left and t2.left:
            self.traverseMerge(t1.left, t2.left, t1, 0)
        
        elif t1.right and not t2.right:
            self.traverseMerge(t1.right, None, t1, 1)

        elif t1.right and t2.right:
            self.traverseMerge(t1.right, t2.right, t1, 1)