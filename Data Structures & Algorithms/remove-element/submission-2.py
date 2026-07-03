class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = k = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] != val:
                left+=1
            elif nums[right] == val:
                right-=1
            else:
                nums[left] = nums[right]
                nums[right] = val
        for num in nums:
            if num == val:
                break
            else:
                k+=1
        return k
            
            