class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # define a min heap with only k elements
        heap = nums
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]