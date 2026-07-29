class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # define a heap and add to the heap with eucliedean distance as a metric
        tmp = []
        for point in points:
            dist = -(point[0]**2 + point[1]**2)**0.5
            tmp.append((dist, point))
        heapq.heapify(tmp)
        while len(tmp) > k:
            heapq.heappop(tmp)
        res = [point for dist,point in tmp]
        return res