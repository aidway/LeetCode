# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Ëã·¨£º Ä£Äâ
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l_tmp = ListNode(l1.val)
                tail.next = l_tmp
                tail = l_tmp
 
                l1 = l1.next
            else:
                l_tmp = ListNode(l2.val)
                tail.next = l_tmp
                tail = l_tmp
                l2 = l2.next
        if l1 is not None:
            tail.next = l1
        if l2 is not None:
            tail.next = l2

        return head.next