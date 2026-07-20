class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # store temperature and index pairs

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                T, index = stack.pop()
                res[index] = i - index
            stack.append((t, i))
        return res


