# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = ""
        num_2 = ""

        while l1:
            num_1 += str(l1.val)
            l1 = l1.next

        while l2:
            num_2 += str(l2.val)
            l2 = l2.next
        
        print("num_1:{} num_2:{}".format(num_1, num_2))
        total = int(num_1[-1::-1]) + int(num_2[-1::-1])
        result = str(total)

        last_node = None
        for i in result:
            new_node = ListNode(i)
            if last_node:
                new_node.next = last_node
            last_node = new_node
        

        return last_node

            