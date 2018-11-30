# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next:
                head_next = head.next
                head.next = None
                return self.reverse(head_next, head)
            
            else:
                return head
            
        return None

    def reverse(self, head, pre):
        if head.next:
            head_next = head.next
            head.next = pre
            return self.reverse(head_next, head)

        else:
            head.next = pre
            return head


    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cursor = head
        answer = None
        while cursor:
            if cursor.next:
                head_next = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = head_next
            else:
                cursor.next = pre
                answer = cursor
                cursor = None
            
        return answer


node1 = ListNode(1)

node2 = ListNode(2)
node1.next = node2

node3 = ListNode(3)
node2.next = node3

print(Solution().reverseList(node1))