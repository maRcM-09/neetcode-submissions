class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        h = {}
        for number in nums:
            h[number] = 1 + h.get(number, 0)
        m = -1
        for n in nums:
            if h[n] == 1 and n > m:
                m = n
        return m