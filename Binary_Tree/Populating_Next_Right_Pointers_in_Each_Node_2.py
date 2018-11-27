class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        same_layer_nodes = []
        if root:
            if root.left:
                same_layer_nodes.append(root.left)

            if root.right:
                same_layer_nodes.append(root.right)

        while(len(same_layer_nodes) > 0):
            new_layer_nodes = []
            for idx, node in enumerate(same_layer_nodes):
                if node.left:
                    new_layer_nodes.append(node.left)

                if node.right:
                    new_layer_nodes.append(node.right)

                if idx < len(same_layer_nodes) - 1:
                    node.next = same_layer_nodes[idx + 1]

            same_layer_nodes = new_layer_nodes
