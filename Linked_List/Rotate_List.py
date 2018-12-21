# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        traverse_queue = []
        origin = head

        while head:
            traverse_queue.append(head)
            head = head.next

        if traverse_queue and k > len(traverse_queue):
            k = k % len(traverse_queue)

        if k == 0 or k == len(traverse_queue):
            return origin

        if len(traverse_queue) > 1 and k < len(traverse_queue):
            traverse_queue[len(traverse_queue) - 1 - k ].next = None
            traverse_queue[len(traverse_queue) - 1].next = traverse_queue[0]
        
        elif len(traverse_queue) == 1:
            return traverse_queue[0]
        
        else:
            return []

        return traverse_queue[len(traverse_queue) - k]