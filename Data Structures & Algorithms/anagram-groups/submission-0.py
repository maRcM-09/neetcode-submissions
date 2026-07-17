class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        def h(ch): # hash function
            return ord(ch) - ord('a')
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[h(c)] += 1
            res[tuple(count)].append(s)
        return list(res.values())