'''
�㷨���ȷŵ�list
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ls = []
        head2 = head
        while head2 is not None:
            ls.append(head2)
            head2 = head2.next
        
        size = len(ls)
        v = size - n
        # ͷ���
        if v == 0:
            head = head.next
            return head
        # β�ڵ�
        elif n == 1:
            ls[v-1].next = None
        else:
            ls[v-1].next = ls[v+1]
        
        return head