import math
class Solution:
    def speed(self,piles,x):
        v_k=0
        for pile in piles:
            v_k+=math.ceil(pile/x)
        return v_k
    def valid(self,x,y):
        return x <= y
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_speed = r
        while l <= r:
            mid = (l+r)//2
            v_mid = self.speed(piles,mid)
            if self.valid(v_mid,h):
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_speed