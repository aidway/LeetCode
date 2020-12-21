'''
算法：模拟
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
 
        if k == 0 or head is None:
            return head
        
        # 找到尾指针和链表长度
        p = tail = head
        n = 0
        while p is not None:
            n += 1
            tail = p
            p = p.next

        # 找到要切断的位置
        k = n - k % n
        n = 1
        p = head
        while p is not None and n < k:
            p = p.next
            n += 1
            
        # 修改链表
        tail.next = head
        head = p.next
        p.next = None
        return head
