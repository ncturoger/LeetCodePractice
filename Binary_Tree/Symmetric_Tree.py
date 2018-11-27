# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        check_list = [root]

        while len(check_list) > 0:
            layer_nodes = []
            for node in check_list:
                if node:
                    node_left = node.left if node.left else None
                    node_right = node.right if node.right else None
                    layer_nodes.append(node_left)
                    layer_nodes.append(node_right)
            for i in range(int(len(layer_nodes)/2)):
                if not layer_nodes[i] and not layer_nodes[-(i+1)]:
                    continue

                elif layer_nodes[i] and layer_nodes[-(i+1)]:
                    if layer_nodes[i].val != layer_nodes[-(i+1)].val:
                        return False
                else:
                    return False

            check_list = layer_nodes
        return True
                     

        