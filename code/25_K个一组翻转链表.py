'''
�㷨��ģ�⡣
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        v = []
        l_head = ListNode()
        l_head.next = head
        tail = l_head
        p = head
        while p is not None:
            v = []
            q = p
            # ��¼k���ڵ㵽list
            for i in range(k):
                if p is None:
                    break
                v.append(p)
                p = p.next
            if len(v) == k:
                # ��k���ڵ���з�ת
                v[0].next = p
                for i in range(len(v)-1, 0, -1):
                    v[i].next = v[i-1]
                tail.next = v[len(v)-1]
                tail = v[0]
            elif len(v) > 0:
                # ���������k���ڵ㣬����ת
                tail.next = q

        return l_head.next
