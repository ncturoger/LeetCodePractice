# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        sorted_array = []
        list_head = head

        while list_head:
            sorted_array.append(list_head.val)
            list_head = list_head.next
        

        return self.create_tree(sorted_array)
    

    def create_tree(self, arr):
        if not arr:
            return None

        node_idx = (len(arr)-1) // 2
        root = TreeNode(arr[node_idx])
        left_part = arr[:node_idx]
        if left_part:
            root.left = self.create_tree(left_part)

        right_part = arr[node_idx+1:]
        if right_part:
            root.right = self.create_tree(right_part)
        
        return root
