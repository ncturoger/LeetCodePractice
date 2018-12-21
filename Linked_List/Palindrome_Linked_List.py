# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        path = []
        if not head:
            return True

        if not head.next:
            return True
        
        while head and head.next:
            path.append(head)
            if head.val == head.next.val:
                if self.goToCompare(head.next, path):
                    return True
            
            if len(path) > 1:
                if path[-2].val == head.next.val:
                    print(head.next.val)
                    
                    for item in path[:-1]:
                        print(item.val)
                    if self.goToCompare(head.next, path[:-1]):
                        return True
                    
            head = head.next
        return False


    def goToCompare(self, head, path):
        while head and path:
            com = path.pop()
            if head.val != com.val:
                return False
            head = head.next

        if path:
            return False
        
        if head and not path:
            return False
        
        return True


node_1 = ListNode()