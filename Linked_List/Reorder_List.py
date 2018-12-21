# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        heads = []
        while head:
            heads.append(head)
            head = head.next
        
        direct = 1
        last_node = None

        while heads:
            if direct == 1:
                node = heads.pop(0)

            else:
                node = heads.pop()
    
            node.next = None
            direct *= -1

            if last_node:
                last_node.next = node
















        # forward_heads = []
        # backward_heads = []

        # direct = 1
        # while head:
        #     if direct == 1:
        #         forward_heads.append(head)

        #     else:
        #         backward_heads.append(head)
               
        #     direct *= -1
        #     head = head.next
        
        # last_head = None
        # first = forward_heads[0]

        # for i in forward_heads:
        #     print("forward_heads:" + str(i.val))

        # for j in backward_heads:
        #     print("backward_heads:" + str(j.val))


        # while forward_heads:
        #     head = forward_heads.pop(0)
        #     if last_head:
        #         last_head.next = head
            
        #     if backward_heads:
        #         head.next = backward_heads.pop()
        #         head.next.next = None
        #         last_head = head.next
            
        #     else:
        #         head.next = None


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print(Solution().reorderList(node_1))