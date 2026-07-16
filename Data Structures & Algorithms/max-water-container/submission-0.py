class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def compute_area(L,R):
            return (R-L)*min(heights[R],heights[L])
        L = 0
        area = 0
        R = len(heights) - 1
        while L < R:
            area = max(area, compute_area(L,R))
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return area
