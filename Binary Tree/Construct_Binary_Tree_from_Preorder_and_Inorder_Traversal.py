# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder = preorder

        node = self.build_tree(inorder)
        
        return node

    def build_tree(self, inorder):
        if len(inorder) > 1:
            root = self.preorder.pop(0)
            root_node = TreeNode(root)
            root_idx = inorder.index(root)
            left_part = inorder[:root_idx]
            right_part = inorder[root_idx+1:]

            if len(left_part) > 0:
                root_node.left = self.build_tree(left_part)

            if len(right_part) > 0:
                root_node.right = self.build_tree(right_part)

            return root_node
        else:
            return TreeNode(self.preorder.pop(0)) if inorder else []
            
