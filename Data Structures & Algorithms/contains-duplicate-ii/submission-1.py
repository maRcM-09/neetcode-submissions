class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contained = set()
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                contained.remove(nums[L])
                L+=1
            if nums[R] in contained:
                return True
            contained.add(nums[R])
        return False