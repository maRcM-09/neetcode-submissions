class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Queue:
    def __init__(self):
        self.left = self.right = None
        self.size = 0
    def enqueue(self, val):
        x = ListNode(val)
        if self.right:
            self.right.next = x # make the connection
            self.right = self.right.next # move the right pointer to end of queue
        else:
            self.left = self.right = x
        self.size += 1
    def dequeue(self):
        if not self.left:
            return None
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        self.size -= 1
        return val

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = Queue()
        sandwiches_stack = []
        n = len(students)
        m = len(sandwiches)
        if n != m:
            return -1
        for i in range(n):
            student_queue.enqueue(students[i])
        for j in range(m):
            sandwiches_stack.append(sandwiches[m-1 - j])
        unsatisfied_counter = 0
        while sandwiches_stack and unsatisfied_counter != student_queue.size:
            student = student_queue.dequeue()
            sandwich = sandwiches_stack[-1]
            if student == sandwich:
                sandwiches_stack.pop()
                unsatisfied_counter = 0
            else:
                student_queue.enqueue(student)
                unsatisfied_counter += 1
        return student_queue.size