class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def max_from_window(L,R):
            s = L
            b = R
            max_w = -float("inf")
            while s <= b:
                max_w = max(max_w , max(nums[s] , nums[b]))
                s+=1
                b-=1
            return max_w
        res = []
        L = 0
        R = k-1
        while R < len(nums):
            res.append(max_from_window(L,R))
            R+=1
            L+=1
        return res