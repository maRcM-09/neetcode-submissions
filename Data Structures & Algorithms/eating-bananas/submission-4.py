class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_speed = r
        while l <= r:
            mid = (l+r)//2
            v_k=0
            for pile in piles:
                v_k+=(pile//mid + min(pile%mid,1))
            valid = v_k <= h
            if valid:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_speed