# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                self.merge(new_node, l1.next, l2)

            elif l2.val < l1.val:
                new_node = ListNode(l2.val)
                self.merge(new_node, l2.next, l1)
            
            return new_node
        
        elif l1:
            return l1
        
        elif l2:
            return l2        



    def merge(self, pre, l1, l2):
        if l1 and l2:
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                pre.next = new_node
                self.merge(new_node, l1.next, l2)

            elif l2.val < l1.val:
                new_node = ListNode(l2.val)
                pre.next = new_node
                self.merge(new_node, l2.next, l1)
        
        elif l1:
            pre.next = l1
        
        elif l2:
            pre.next = l2