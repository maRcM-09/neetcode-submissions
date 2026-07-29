class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        # get the two largest:
        while len(heap) > 1:
            # retrieve the two largest stones
            y = heapq.heappop_max(heap)
            x = heapq.heappop_max(heap)
            # smash them
            if x == y:
                continue
            elif x < y:
                heapq.heappush_max(heap, y-x)
        if len(heap) == 0:
            return 0
        return heap[0]
