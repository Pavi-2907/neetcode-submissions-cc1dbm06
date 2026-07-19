# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        values.sort()

        dummy = ListNode(0)
        cur = dummy
        for val in values:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
        