# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        n = len(arr)
        k%=n

        arr = arr[-k:] + arr[:-k]

        dummy = ListNode(0)
        cur = dummy
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next
            
        return dummy.next