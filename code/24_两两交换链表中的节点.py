'''
算法：模拟，具体见题解。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        l_head = ListNode()
        l_head.next = head
        tail = l_head
        p = head
        while p is not None:
            q = p.next
            if q is None:
                break
            k = q.next
            q.next = p
            p.next = k
            tail.next = q
            tail = tail.next.next
            p = p.next

        return l_head.next