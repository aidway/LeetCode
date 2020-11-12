# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        bit = 0
        l_head = ListNode(-1)
        l_tail = l_head
        while l1 is not None or l2 is not None:
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0

            n3 = n1 + n2 + bit
            val = n3 % 10        # 当前位的数值
            bit = int(n3 / 10)   # 进位

            l_tmp = ListNode(val)
            l_tail.next = l_tmp
            l_tail = l_tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if bit > 0:
            l_tmp = ListNode(bit)
            l_tail.next = l_tmp
            l_tail = l_tail.next
        return l_head.next