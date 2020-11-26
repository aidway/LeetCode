'''
Ëã·¨£º¿ìÂýÖ¸Õë¡£
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        q = p = head
        while p is not None and q is not None:
            p = p.next
            q = q.next
            if q is None:
                return False
            q = q.next
            if p == q:
                return True
        return False