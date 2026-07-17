# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        cur,tail = head , head.next
        while tail.next.next:
            tail = tail.next
        # now we have left and right pointers
        node_to_change = tail.next
        tail.next = None
        node_to_change.next = cur.next
        cur.next = node_to_change
        
        self.reorderList(node_to_change.next)
