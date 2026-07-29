class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0] + nums
        self.k = k
        self.heapify()
        while len(self.heap) > self.k + 1:
            self.pop()

    def pop(self):
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.perculate_down(1)

    def perculate_up(self):
       i = len(self.heap) - 1
       while i > 1 and self.heap[i] < self.heap[i//2]:
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp
            i = i//2 

    def perculate_down(self , i):

        while 2*i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i + 1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]:
                tmp = self.heap[2*i+1]
                self.heap[2*i+1] = self.heap[i]
                self.heap[i] = tmp
                i=2*i+1
            elif self.heap[i] > self.heap[2*i]:
                tmp = self.heap[2*i]
                self.heap[2*i] = self.heap[i]
                self.heap[i] = tmp
                i=2*i
            else:
                break

    def heapify(self):
        cur = (len(self.heap)-1)//2
        while cur > 0:
            i = cur
            self.perculate_down(i)
            cur = cur - 1

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.perculate_up()

        if len(self.heap) - 1 > self.k:
            self.pop()
        return self.heap[1]
        # now return kth largest

