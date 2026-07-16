class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        index = 1

        for el in nums[1:]:
            if el != prev:
                nums[index] = el
                index += 1
            prev = el

        return index