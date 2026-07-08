# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(L1, L2):
    dummy = ListNode(0)
    tail = dummy
    while L1 and L2:
        if L1.val < L2.val:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 if L1 else L2
    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k==0 or not lists:
            return None
        elif k == 1:
            return lists[0]
        elif k ==2:
            return merge(lists[0],lists[1])

        m = (k)//2
        list_left = self.mergeKLists(lists[:m])
        list_right = self.mergeKLists(lists[m:])
        return self.mergeKLists([list_left , list_right])