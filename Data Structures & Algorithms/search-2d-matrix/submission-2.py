class Solution:
    def convert_to_coordinates(self, x , cols):
        return x//cols , x%cols
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix) , len(matrix[0])
        left , right = 0 , m*n - 1
        while left <= right:
            mid = (left + right)//2
            row_k , col_k = self.convert_to_coordinates(mid , n)
            if matrix[row_k][col_k] < target:
                left = mid+1
            elif matrix[row_k][col_k]>target:
                right = mid-1
            else:
                return True
        return False
