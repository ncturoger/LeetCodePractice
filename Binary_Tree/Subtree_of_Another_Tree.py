# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s and t:
            check_list = [s]

            while check_list:
                new_check_list = []
                for node in check_list:
                    if node.val == t.val:
                        if self.check_sub(node, t):
                            return True
                    if node.right:
                        new_check_list.append(node.right)
                    
                    if node.left:
                        new_check_list.append(node.left)
                    
                check_list = new_check_list
            
            return False

        else:
            return False

    
    def check_sub(self, s, t):
        check_list = [s]
        target_list = [t]

        while check_list:
            if len(check_list) != len(target_list):
                return False

            new_check_list = []
            new_target_list = []
 
            for idx, node in enumerate(check_list):
                if node.val !=  target_list[idx].val:
                    return False
                
                if not node.left and target_list[idx].left:
                    return False
                
                if node.left  and not target_list[idx].left:
                    return False

                if not node.right and target_list[idx].right:
                    return False
                
                if node.right and not target_list[idx].right:
                    return False


                if node.left and target_list[idx].left:
                    new_check_list.append(node.left)
                    new_target_list.append(target_list[idx].left)
                    
                if node.right and target_list[idx].right:
                    new_check_list.append(node.right)
                    new_target_list.append(target_list[idx].right)                    
                    

            check_list = new_check_list
            target_list = new_target_list
        
        return True

