# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        arr.sort()

        dummy = ListNode(0)
        cur = dummy 
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
        