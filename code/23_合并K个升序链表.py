'''
算法：每次选一个最小值。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        head = ListNode()
        tail = head
        while True:
            ok = False
            v = 999999
            for i in range(n):
                if lists[i] is not None:
                    if lists[i].val < v:
                        ok = True
                        v = lists[i].val
                        tmp = i
            if ok == False:
                break
            l_tmp = ListNode(lists[tmp].val)
            lists[tmp] = lists[tmp].next
            tail.next = l_tmp
            tail = l_tmp
            
        return head.next