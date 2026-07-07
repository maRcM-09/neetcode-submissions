class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)

        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        i = 0
        for _ in range(index):
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size , val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0: 
            index = 0
        if index > self.size:
            return
        curr = self.head.next
        val_node = ListNode(val)
        for _ in range(index):
            curr = curr.next

        prev_node = curr.prev
        prev_node.next = val_node
        val_node.prev = prev_node

        val_node.next = curr
        curr.prev = val_node

        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        prev_node , next_node = curr.prev , curr.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)