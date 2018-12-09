# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        last_node = None
        while head:
            if head.val == node.val:
                last_node.next = node.next
            
            last_node = head
            head = head.next

