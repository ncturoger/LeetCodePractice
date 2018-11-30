# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 1
        pre = None
        first = head

        while head:
            if count == 1:
                pre = head
                head = head.next
                
            
            else:
                head_val = head.val
                head.val = pre.val
                pre.val = head_val
                pre = head
                head = head.next
            count *= -1
        
    
        return first


