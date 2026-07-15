class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        comb, res = [] , []
        def dfs(i, total):
            if total == target:
                res.append(comb[:])
                return
            if i >= len(candidates) or total > target:
                return
            # Option 1: include the number and try next
            comb.append(candidates[i])
            dfs(i+1, total + candidates[i])
            comb.pop()
            # Skip duplicates to avoid TLE and duplicate results
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)
        dfs(0,0)
        return res