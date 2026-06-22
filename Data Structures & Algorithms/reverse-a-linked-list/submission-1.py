# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next
            
        values.reverse()

        dummy = ListNode(0)
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next