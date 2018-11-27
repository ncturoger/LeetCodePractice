# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
            return list(same_path)[-1]


    def get_path(self, node, target):
        path = []
        walked = []
        locate = node
        while locate.val != target.val:
            path.append(locate)
            walked.append(locate)

            if locate.left and locate.left not in walked:
                locate = locate.left
            
            elif locate.right and locate.right not in walked:
                locate = locate.right
            
            else:
                path.pop()
                locate = path[-1]
        
        return path

            


node_1 = TreeNode(3)
node_2 = TreeNode(5)
node_3 = TreeNode(1)
node_4 = TreeNode(6)
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4

for node in Solution().get_path(node_1, node_3):
    print(node.val)






