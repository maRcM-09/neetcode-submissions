class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L , R = 0 , len(nums) - 1
        mid = (L+R)//2
        while L <= R:
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
            mid = (L+R)//2
        return -1