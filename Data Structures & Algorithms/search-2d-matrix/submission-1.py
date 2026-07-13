class Solution:
    def binary_search(self, nums, target):
        L , R = 0, len(nums)-1
        mid = (L+R)//2
        while L<=R:
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return True
            mid = (L+R)//2
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target < row[-1] and target > row[0]:
                return self.binary_search(row, target)
            elif target == row[-1]:
                return True
            elif target == row[0]:
                return True
        return False
